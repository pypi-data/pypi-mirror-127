import datetime
import logging
import os
import tempfile
import warnings

import numpy as np

from pathlib import Path

from small_text.classifiers.classification import EmbeddingMixin
from small_text.data.datasets import split_data
from small_text.integrations.pytorch.exceptions import PytorchNotFoundError
from small_text.utils.context import build_pbar_context
from small_text.utils.data import list_length
from small_text.utils.datetime import format_timedelta
from small_text.utils.logging import verbosity_logger, VERBOSITY_MORE_VERBOSE
from small_text.utils.system import get_tmp_dir_base


try:
    import torch
    import torch.nn.functional as F

    from torch import randperm
    from torch.optim.lr_scheduler import _LRScheduler
    from torch.nn.modules import CrossEntropyLoss, BCEWithLogitsLoss
    from torch.utils.data import DataLoader

    from small_text.integrations.pytorch.classifiers.base import PytorchClassifier
    from small_text.integrations.pytorch.model_selection import Metric, PytorchModelSelection
    from small_text.integrations.pytorch.utils.data import dataloader, get_class_weights
    from small_text.integrations.transformers.datasets import TransformersDataset
except ImportError:
    raise PytorchNotFoundError('Could not import pytorch')


from transformers import AdamW, get_linear_schedule_with_warmup
from transformers import AutoConfig, AutoModelForSequenceClassification, AutoTokenizer


def transformers_collate_fn(batch):
    with torch.no_grad():
        text = torch.cat([entry[TransformersDataset.INDEX_TEXT] for entry in batch], dim=0)
        masks = torch.cat([entry[TransformersDataset.INDEX_MASK] for entry in batch], dim=0)
        label = torch.tensor([entry[TransformersDataset.INDEX_LABEL] for entry in batch])

    return text, masks, label


class FineTuningArguments(object):
    """
    Arguments to enable and configure gradual unfreezing and discriminative learning rates as used in
    Universal Language Model Fine-tuning (ULMFiT) [HR18]_.

    References
    ----------
    .. [HR18] Jeremy Howard and Sebastian Ruder
       Universal Language Model Fine-tuning for Text Classification.
       In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics, 2008, 328–339.
    """

    def __init__(self, base_lr, layerwise_gradient_decay, gradual_unfreezing=-1, cut_fraction=0.1):

        if base_lr <= 0:
            raise ValueError('FineTuningArguments: base_lr must be greater than zero')
        if layerwise_gradient_decay:
            if not (0 < layerwise_gradient_decay < 1 or layerwise_gradient_decay == -1):
                raise ValueError('FineTuningArguments: valid values for layerwise_gradient_decay '
                                 'are between 0 and 1 (or set it to -1 to disable it)')

        self.base_lr = base_lr
        self.layerwise_gradient_decay = layerwise_gradient_decay

        self.gradual_unfreezing = gradual_unfreezing
        self.cut_fraction = cut_fraction


class TransformerModelArguments(object):

    def __init__(self, model, tokenizer=None, config=None):
        self.model = model
        self.tokenizer = tokenizer
        self.config = config

        if self.tokenizer is None:
            self.tokenizer = model
        if self.config is None:
            self.config = model


def _get_layer_params(model, base_lr, fine_tuning_arguments):

    layerwise_gradient_decay = fine_tuning_arguments.layerwise_gradient_decay

    params = []

    base_model = getattr(model, model.base_model_prefix)
    if hasattr(base_model, 'encoder'):
        layers = base_model.encoder.layer
    else:
        layers = base_model.transformer.layer

    total_layers = len(layers)

    use_gradual_unfreezing = isinstance(fine_tuning_arguments.gradual_unfreezing, int) and \
        fine_tuning_arguments.gradual_unfreezing > 0

    start_layer = 0 if not use_gradual_unfreezing else total_layers-fine_tuning_arguments.gradual_unfreezing
    num_layers = total_layers - start_layer

    for i in range(start_layer, total_layers):
        lr = base_lr if not layerwise_gradient_decay else base_lr * layerwise_gradient_decay ** (
                    num_layers - i)
        params.append({
            'params': layers[i].parameters(),
            'lr': lr
        })

    return params


class TransformerBasedEmbeddingMixin(EmbeddingMixin):

    EMBEDDING_METHOD_AVG = 'avg'
    EMBEDDING_METHOD_CLS_TOKEN = 'cls'

    def embed(self, data_set, return_proba=False, embedding_method=EMBEDDING_METHOD_AVG,
              hidden_layer_index=-1, pbar='tqdm'):
        """
        Embeds each sample in the given `data_set`.

        The embedding is created by using hidden representation from the transformer model's
        representation in the hidden layer at the given `hidden_layer_index`.

        Parameters
        ----------
        return_proba : bool
            Also return the class probabilities for `data_set`.
        embedding_method : str
            Embedding method to use [avg, cls].
        hidden_layer_index : int
            Index of the hidden layer.
        pbar : str or None
            The progress bar to use, or None otherwise.

        Returns
        -------
        embeddings : np.ndarray
            Embeddings in the shape (N, hidden_layer_dimensionality).
        proba : np.ndarray
            Class probabilities for `data_set` (only if `return_predictions` is `True`).
        """

        if self.model is None:
            raise ValueError('Model is not trained. Please call fit() first.')

        self.model.eval()

        train_iter = dataloader(data_set.data, self.mini_batch_size, self._create_collate_fn(),
                                train=False)

        tensors = []
        predictions = []

        with build_pbar_context(pbar, tqdm_kwargs={'total': list_length(data_set)}) as pbar:
            for batch in train_iter:
                batch_len, logits = self._create_embeddings(tensors,batch,
                                                            embedding_method=embedding_method,
                                                            hidden_layer_index=hidden_layer_index)
                pbar.update(batch_len)
                if return_proba:
                    predictions.extend(F.softmax(logits, dim=1).detach().to('cpu').tolist())

        if return_proba:
            return np.array(tensors), np.array(predictions)

        return np.array(tensors)

    def _create_embeddings(self, tensors, batch, embedding_method='avg', hidden_layer_index=-1):

        text, masks, _ = batch
        text = text.to(self.device, non_blocking=True)
        masks = masks.to(self.device, non_blocking=True)

        outputs = self.model(text,
                             token_type_ids=None,
                             attention_mask=masks,
                             output_hidden_states=True)

        # only use states of hidden layers, excluding the token embeddings
        hidden_states = outputs.hidden_states[1:]

        if embedding_method == self.EMBEDDING_METHOD_CLS_TOKEN:
            representation = hidden_states[hidden_layer_index][:, 0]
        elif embedding_method == self.EMBEDDING_METHOD_AVG:
            representation = torch.mean(hidden_states[hidden_layer_index][:, 1:], dim=1)
        else:
            raise ValueError(f'Invalid embedding_method: {embedding_method}')

        tensors.extend(representation.detach().to('cpu', non_blocking=True).numpy())

        return text.size(0), outputs.logits


class TransformerBasedClassification(TransformerBasedEmbeddingMixin, PytorchClassifier):

    def __init__(self, transformer_model, num_classes, num_epochs=10, lr=2e-5,
                 mini_batch_size=12, criterion=None, optimizer=None, scheduler='linear',
                 validation_set_size=0.1, validations_per_epoch=1, no_validation_set_action='sample',
                 initial_model_selection=None, early_stopping_no_improvement=5,
                 early_stopping_acc=-1, model_selection=True, fine_tuning_arguments=None,
                 device=None, memory_fix=1, class_weight=None,
                 verbosity=VERBOSITY_MORE_VERBOSE, cache_dir='.active_learning_lib_cache/'):
        """
        Parameters
        ----------
        transformer_model : TransformerModelArguments
            Settings for transformer model, tokenizer and config.
        num_classes : int
            Number of classes.
        num_epochs : int
            Epochs to train.
        lr : float
            Learning rate.
        mini_batch_size : int
            Size of mini batches during training.
        criterion :

        optimizer :

        scheduler :

        validation_set_size : float
            The sizes of the validation as a fraction of the training set if no validation set
            is passed and `no_validation_set_action` is set to 'sample'.
        validations_per_epoch : int
            Defines how of the validation set is evaluated during the training of a single epoch.
        no_validation_set_action : {'sample', 'none}
            Defines what should be done of no validation set is given.
        initial_model_selection :

        early_stopping_no_improvement :

        early_stopping_acc :

        model_selection :

        fine_tuning_arguments : FineTuningArguments

        device : str or torch.device
            Torch device on which the computation will be performed.
        memory_fix : int
            If this value if greater zero, every `memory_fix`-many epochs the cuda cache will be
            emptied to force unused GPU memory being released.

        class_weight : 'balanced' or None

        """
        super().__init__(device=device)

        if criterion is not None and class_weight is not None:
            warnings.warn('Class weighting will have no effect with a non-default criterion',
                          RuntimeWarning)

        with verbosity_logger():
            self.logger = logging.getLogger(__name__)
            self.logger.verbosity = verbosity

        # Training parameters
        self.num_classes = num_classes
        self.num_epochs = num_epochs
        self.lr = lr
        self.mini_batch_size = mini_batch_size
        self.criterion = criterion
        self.optimizer = optimizer
        self.scheduler = scheduler

        self.validation_set_size = validation_set_size
        self.validations_per_epoch = validations_per_epoch
        # 'sample' or 'none'
        self.no_validation_set_action = no_validation_set_action
        self.initial_model_selection = initial_model_selection

        # Huggingface
        self.transformer_model = transformer_model

        # Other
        self.early_stopping_no_improvement = early_stopping_no_improvement
        self.early_stopping_acc = early_stopping_acc
        self.class_weight = class_weight

        self.model_selection = model_selection
        self.fine_tuning_arguments = fine_tuning_arguments

        self.memory_fix = memory_fix
        self.verbosity = verbosity
        self.cache_dir = cache_dir

        self.model = None
        self.model_selection_manager = None

    def fit(self, train_set, validation_set=None, optimizer=None, scheduler=None):
        """
        Parameters
        ----------
        train_set : TransformersDataset
            Training set.

        Returns
        -------
        self : HuggingfaceTransformersClassification
            Returns the current HuggingfaceTransformersClassification instance with a trained model.
        """
        if (train_set.y == TransformersDataset.NO_LABEL).any():
            raise ValueError('Training labels must not be None')
        if validation_set is not None and \
                (validation_set.y == TransformersDataset.NO_LABEL).any():
            raise ValueError('Validation set labels must not be None')

        if validation_set is None and self.no_validation_set_action == 'sample':
            sub_train, sub_valid = split_data(train_set, y=train_set.y, strategy='balanced',
                                              validation_set_size=self.validation_set_size)
        elif validation_set is None and self.no_validation_set_action == 'none':
            sub_train, sub_valid = train_set, None
        else:
            sub_train, sub_valid = train_set, validation_set

        fit_scheduler = scheduler if scheduler is not None else self.scheduler
        fit_optimizer = optimizer if optimizer is not None else self.optimizer

        self.class_weights_ = self.initialize_class_weights(sub_train)

        return self._fit_main(sub_train, sub_valid, fit_optimizer, fit_scheduler)

    def initialize_class_weights(self, sub_train):
        if self.class_weight == 'balanced':
            class_weights_ = get_class_weights(sub_train.y, self.num_classes)
            class_weights_ = class_weights_.to(self.device)
        else:
            class_weights_ = None
        return class_weights_

    def _fit_main(self, sub_train, sub_valid, optimizer, scheduler):
        if self.model is None:
            y = [entry[TransformersDataset.INDEX_LABEL] for entry in sub_train]
            if self.num_classes is None:
                self.num_classes = np.max(y) + 1

            if self.num_classes != np.max(y) + 1:
                raise ValueError('Conflicting information about the number of classes: '
                                 'expected: {}, encountered: {}'.format(self.num_classes,
                                                                        np.max(y) + 1))

            self.initialize_transformer(self.cache_dir)

        if self.criterion is None:
            self.criterion = self.get_default_criterion()

        if self.fine_tuning_arguments is not None:
            params = _get_layer_params(self.model, self.lr, self.fine_tuning_arguments)
        else:
            params = None

        if optimizer is None or scheduler is None:
            if optimizer is not None:
                self.logger.warning('Overridering optimizer since optimizer in kwargs needs to be '
                               'passed in combination with scheduler')
            if scheduler is not None:
                self.logger.warning('Overridering scheduler since optimizer in kwargs needs to be '
                                    'passed in combination with scheduler')

            optimizer, scheduler = self._initialize_optimizer_and_scheduler(optimizer,
                                                                            scheduler,
                                                                            self.fine_tuning_arguments,
                                                                            self.lr,
                                                                            params,
                                                                            self.model,
                                                                            sub_train)

        self.model = self.model.to(self.device)

        with tempfile.TemporaryDirectory(dir=get_tmp_dir_base()) as tmp_dir:
            res = self._train(sub_train, sub_valid, tmp_dir, optimizer, scheduler)
            self._perform_model_selection(sub_valid)

        return res

    def initialize_transformer(self, cache_dir):

        self.config = AutoConfig.from_pretrained(
            self.transformer_model.config,
            num_labels=self.num_classes,
            cache_dir=cache_dir,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.transformer_model.tokenizer,
            cache_dir=cache_dir,
        )
        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.transformer_model.model,
            from_tf=False,
            config=self.config,
            cache_dir=cache_dir,
        )

    def _initialize_optimizer_and_scheduler(self, optimizer, scheduler, fine_tuning_arguments,
                                            base_lr, params, model, sub_train):

        steps = (len(sub_train) // self.mini_batch_size) \
                + int(len(sub_train) % self.mini_batch_size != 0)

        if params is None:
            params = [param for param in model.parameters() if param.requires_grad]

        optimizer = self._default_optimizer(params, base_lr) if optimizer is None else optimizer

        if scheduler == 'linear':
            scheduler = get_linear_schedule_with_warmup(optimizer,
                                                        num_warmup_steps=0,
                                                        num_training_steps=steps*self.num_epochs)
        elif not isinstance(scheduler, _LRScheduler):
            raise ValueError(f'Invalid scheduler: {scheduler}')

        return optimizer, scheduler

    def _default_optimizer(self, params, base_lr):
        return AdamW(params, lr=base_lr, eps=1e-8)

    def _train(self, sub_train, sub_valid, tmp_dir, optimizer, scheduler):

        if self.initial_model_selection:
            if sub_valid is None:
                raise ValueError('Error! Initial model selection requires a validation set')

            with tempfile.TemporaryDirectory(dir=get_tmp_dir_base()) as mselection_tmp_dir:
                self._perform_initial_model_selection(sub_train, sub_valid, mselection_tmp_dir)
            start_epoch = self.initial_model_selection[1]
        else:
            start_epoch = 0

        metrics = [Metric('valid_loss', True), Metric('valid_acc', False),
                   Metric('train_loss', True), Metric('train_acc', False)]
        self.model_selection_manager = PytorchModelSelection(Path(tmp_dir), metrics)

        self._train_loop(sub_train, sub_valid, optimizer, scheduler, start_epoch, self.num_epochs,
                         self.model_selection_manager)

        return self

    # TODO: uses default optimizer and scheduler for now
    def _perform_initial_model_selection(self, sub_train, sub_valid, tmp_dir):

        num_models = self.initial_model_selection[0]
        num_epochs = self.initial_model_selection[1]

        metrics = [Metric('valid_loss', True), Metric('valid_acc', False),
                   Metric('train_loss', True), Metric('train_acc', False)]

        model_selection_managers = []

        for j in range(num_models):

            tmp_dir_local = Path(tmp_dir).joinpath(f'{j}/').absolute()
            os.mkdir(tmp_dir_local)

            model_selection_manager = PytorchModelSelection(Path(tmp_dir_local), metrics)
            self.initialize_transformer(self.cache_dir)
            self.model = self.model.to(self.device)

            # add initial entry since we want to restore the first model at the end
            fill = dict({metric.name: float('inf') if metric.lower_is_better else float('-inf')
                         for metric in metrics})
            model_selection_manager.add_model(self.model, 0, **fill)


            optimizer_mod, scheduler_mod = self._initialize_optimizer_and_scheduler(None,
                                                                                    'linear',
                                                                                    self.fine_tuning_arguments,
                                                                                    self.lr,
                                                                                    None,
                                                                                    self.model,
                                                                                    sub_train)

            self._train_loop(sub_train, sub_valid, optimizer_mod, scheduler_mod, 0, num_epochs, model_selection_manager)
            model_selection_managers.append(model_selection_manager)

        # relativ to metric list above
        target_metric = 0

        best_metric = None
        best_model = -1

        for j, model_selection_manager in enumerate(model_selection_managers):
            model_path, model_metrics = model_selection_manager.select_best()

            if best_metric is None:
                best_metric = model_metrics[target_metric]
                best_model = j
            else:
                if metrics[target_metric].lower_is_better:
                    is_better = model_metrics[target_metric] < best_metric
                else:
                    is_better = model_metrics[target_metric] > best_metric

                if is_better:
                    best_metric = model_metrics[target_metric]
                    best_model = j

        # load the first model (untrained) from the best selection process
        best_key = list(model_selection_managers[best_model].models.keys())[0]
        self.model.load_state_dict(torch.load(model_selection_managers[best_model].models[best_key]))

    def _train_loop(self, sub_train, sub_valid, optimizer, scheduler, start_epoch, num_epochs,
                    model_selection_manager):

        min_loss = float('inf')
        no_loss_reduction = 0

        stopped = False

        for epoch in range(start_epoch, num_epochs):
            start_time = datetime.datetime.now()

            if self.memory_fix and (epoch + 1) % self.memory_fix == 0:
                torch.cuda.empty_cache()

            self.model.train()

            # TODO: extract this block after introducing a shared return type
            if self.validations_per_epoch > 1:
                num_batches = len(sub_train) // self.mini_batch_size \
                              + int(len(sub_train) % self.mini_batch_size > 0)
                if self.validations_per_epoch > num_batches:
                    warnings.warn(
                        f'validations_per_epoch={self.validations_per_epoch} is greater than '
                        f'the maximum possible batches of {num_batches}',
                        RuntimeWarning)
                    validate_every = 1
                else:
                    validate_every = int(num_batches / self.validations_per_epoch)

                train_loss, train_acc, valid_loss, valid_acc = self._train_loop_process_batches(
                    sub_train,
                    optimizer,
                    scheduler,
                    validate_every=validate_every,
                    validation_set=sub_valid)
            else:
                train_loss, train_acc = self._train_loop_process_batches(
                    sub_train,
                    optimizer,
                    scheduler)

                if sub_valid is not None:
                    valid_loss, valid_acc = self.validate(sub_valid)

            timedelta = datetime.datetime.now() - start_time

            self._log_epoch(epoch, timedelta, sub_train, sub_valid, train_acc, train_loss,
                            valid_acc, valid_loss)

            if sub_valid is not None:
                # TODO: early stopping configurable
                if self.early_stopping_no_improvement > 0:
                    if valid_loss < min_loss:
                        no_loss_reduction = 0
                        min_loss = valid_loss
                    else:
                        no_loss_reduction += 1

                        if no_loss_reduction >= self.early_stopping_no_improvement:
                            print('\nEarly stopping after %s epochs' % (epoch + 1))
                            stopped = True

                if not stopped and self.early_stopping_acc > 0:
                    if train_acc > self.early_stopping_acc:
                        print('\nEarly stopping due to high train acc: %s' % (train_acc))
                        stopped = True

                model_selection_manager.add_model(self.model, epoch + 1, valid_acc=valid_acc,
                                                  valid_loss=valid_loss, train_acc=train_acc,
                                                  train_loss=train_loss)

            if stopped:
                break

    def _train_loop_process_batches(self, sub_train_, optimizer, scheduler, validate_every=None,
                                    validation_set=None):

        train_loss = 0.
        train_acc = 0.
        valid_losses = []
        valid_accs = []

        train_iter = dataloader(sub_train_.data, self.mini_batch_size, self._create_collate_fn())

        for i, (text, masks, cls) in enumerate(train_iter):
            loss, acc = self._train_single_batch(text, masks, cls, optimizer)
            scheduler.step()

            train_loss += loss
            train_acc += acc

            if validate_every and i % validate_every == 0:
                valid_loss, valid_acc = self.validate(validation_set)
                valid_losses.append(valid_loss)
                valid_accs.append(valid_acc)

        if validate_every:
            return train_loss / len(sub_train_), train_acc / len(sub_train_), \
                   np.mean(valid_losses), np.mean(valid_accs)
        else:
            return train_loss / len(sub_train_), train_acc / len(sub_train_)

    def _create_collate_fn(self):
        return transformers_collate_fn

    def _train_single_batch(self, text, masks, cls, optimizer):

        train_loss = 0.
        train_acc = 0.

        optimizer.zero_grad()

        text, masks, cls = text.to(self.device), masks.to(self.device), cls.to(self.device)
        outputs = self.model(text, attention_mask=masks)

        if self.num_classes == 2:
            logits = outputs.logits
            target = F.one_hot(cls, 2).float()
        else:
            logits = outputs.logits.view(-1, self.num_classes)
            target = cls

        loss = self.criterion(logits, target)

        loss.backward()

        torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)

        optimizer.step()

        train_loss += loss.detach().item()
        train_acc += (logits.argmax(1) == cls).sum().detach().item()

        del text, masks, cls, loss, outputs

        return train_loss, train_acc

    def _perform_model_selection(self, sub_valid):
        if sub_valid is not None:
            if self.model_selection:
                self._select_best_model()
            else:
                self._select_last_model()

    def _select_best_model(self):
        model_path, _ = self.model_selection_manager.select_best()
        self.model.load_state_dict(torch.load(model_path))

    def _select_last_model(self):
        model_path, _ = self.model_selection_manager.select_last()
        self.model.load_state_dict(torch.load(model_path))

    def _log_epoch(self, epoch, timedelta, sub_train, sub_valid, train_acc, train_loss, valid_acc, valid_loss):
        if sub_valid is not None:
            valid_loss_txt = f'\n\tLoss: {valid_loss:.4f}(valid)\t|\tAcc: {valid_acc * 100:.1f}%(valid)'
        else:
            valid_loss_txt = ''
        self.logger.info(f'Epoch: {epoch + 1} | {format_timedelta(timedelta)}\n'
                         f'\tTrain Set Size: {len(sub_train)}\n'
                         f'\tLoss: {train_loss:.4f}(train)\t|\tAcc: {train_acc * 100:.1f}%(train)'
                         f'{valid_loss_txt}',
                         verbosity=VERBOSITY_MORE_VERBOSE)

    def validate(self, validation_set):

        valid_loss = 0.
        acc = 0.

        self.model.eval()
        valid_iter = dataloader(validation_set.data, self.mini_batch_size, self._create_collate_fn(),
                                train=False)

        for x, masks, cls in valid_iter:
            x, masks, cls = x.to(self.device), masks.to(self.device), cls.to(self.device)

            with torch.no_grad():
                outputs = self.model(x, attention_mask=masks, labels=cls)

                valid_loss += outputs.loss.item()
                acc += (outputs.logits.argmax(1) == cls).sum().item()
                del outputs, x, masks, cls

        return valid_loss / len(validation_set), acc / len(validation_set)

    def predict(self, test_set, return_proba=False):
        if len(test_set) == 0:
            if return_proba:
                return np.array([], dtype=int), np.array([], dtype=float)
            return np.array([], dtype=int)

        proba = self.predict_proba(test_set)
        predictions = np.argmax(proba, axis=1)

        if return_proba:
            return predictions, proba

        return predictions

    def predict_proba(self, test_set):
        if len(test_set) == 0:
            return np.array([], dtype=int), np.array([], dtype=float)

        self.model.eval()
        test_iter = dataloader(test_set.data, self.mini_batch_size, self._create_collate_fn(),
                               train=False)

        predictions = []

        with torch.no_grad():
            for text, masks, _ in test_iter:
                text, masks = text.to(self.device), masks.to(self.device)
                outputs = self.model(text, attention_mask=masks)
                predictions += F.softmax(outputs.logits, dim=1).detach().to('cpu').tolist()
                del text, masks

        return np.array(predictions)

    def __del__(self):
        try:
            del self.criterion, self.optimizer, self.scheduler
            del self.model, self.tokenizer, self.config
        except:
            pass
