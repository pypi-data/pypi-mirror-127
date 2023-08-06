import logging

from abc import abstractmethod

from small_text.classifiers.classification import Classifier
from small_text.integrations.pytorch.exceptions import PytorchNotFoundError

try:
    import torch

    from torch.nn.modules import CrossEntropyLoss, BCEWithLogitsLoss
except ImportError:
    raise PytorchNotFoundError('Could not import pytorch')


logger = logging.getLogger(__name__)


class PytorchClassifier(Classifier):

    def __init__(self, device=None):

        if device is None:
            self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        else:
            self.device = device

        if self.device.startswith('cuda'):
            logging.info('torch.version.cuda: %s', torch.version.cuda)
            logging.info('torch.cuda.is_available(): %s', torch.cuda.is_available())
            if torch.cuda.is_available():
                logging.info('torch.cuda.current_device(): %s', torch.cuda.current_device())

    @abstractmethod
    def fit(self, train_set, validation_set=None, **kwargs):
        pass

    @abstractmethod
    def predict(self, test_set, return_proba=False):
        """
        Parameters
        ----------
        test_set : small_text.integrations.pytorch.PytorchTextClassificationDataset
            Test set.
        return_proba : bool
            If True, additionally returns the confidence distribution over all classes.

        Returns
        -------
        predictions : np.ndarray
            List of predictions.
        scores : np.ndarray (optional)
            Distribution of confidence scores over all classes if `return_proba` is True.
        """
        pass

    @abstractmethod
    def predict_proba(self, test_set):
        """
        Parameters
        ----------
        test_set : small_text.integrations.pytorch.PytorchTextClassificationDataset
            Test set.

        Returns
        -------
        scores : np.ndarray
            Distribution of confidence scores over all classes.
        """
        pass

    def get_default_criterion(self):
        if self.num_classes == 2:
            return BCEWithLogitsLoss(pos_weight=self.class_weights_)
        else:
            return CrossEntropyLoss(weight=self.class_weights_)
