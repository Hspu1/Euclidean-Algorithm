"""
:author: Hspu1
:license: MIT
:copyright: (c) 2024 Hspu1
"""

__all__ = (
    "euclidean_algorithm",
    "EuclideanAlgorithmValueError",
    "EuclideanAlgorithmLengthError"
)


from .euclidean_algorithm import euclidean_algorithm
from .exceptions import (
    EuclideanAlgorithmValueError, EuclideanAlgorithmLengthError
)

__author__ = "Hspu1"
__version__ = "0.1.1"
__email__ = "rumyantsev1m0s1@gmail.com"
