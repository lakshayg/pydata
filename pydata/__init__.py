"""
PyData is a minimal python module to work with classification datasets.
It provides publicly available datasets in a ready to use manner within
python. It also contains utility functions for common dataset operations.
The source code is available at <https://github.com/lakshayg/pydata>.
"""
from datasets import load_banana
from datasets import load_cifar10
from datasets import load_magic04
from datasets import load_letters
from datasets import load_usps
from datasets import load_forest_cover
from datasets import load_mnist

from utils import norm_minmax
from utils import norm_zscore
from utils import shuffle
from utils import random_sample

