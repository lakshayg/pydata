"""
This module contains various utility functions for use on
datsets. These are convenience functions which provide
oneliners for commonly used operations.
"""
import numpy as np

def norm_minmax(X, low=-1, high=1):
    """
    Scale and shift a dataset such that it lies in the
    bounds specified by its arguments `low` and `high`
    """
    assert low < high
    m1 = np.min(X)
    m2 = np.max(X)
    return (X-m1)/(m2 - m1) * (high-low) + low

def norm_zscore(X):
    """
    Centers the data by substracting mean from all the
    datapoints and dividing by standard deviation
    """
    mu = np.mean(X)
    sigma = np.std(X)
    return (X - mu)/sigma

def shuffle(X, y):
    """
    Shuffles the data and its labels in a random permutation
    """
    indices = np.random.permutation(X.shape[0])
    XX = X[indices,:]
    yy = y[indices]
    return XX, yy

def random_sample(X, y, n_samples=1):
    """
    Samples a small subset from the complete data. The number
    of datapoints to be sampled is specified by the `n_samples`
    parameter.
    """
    indices = np.random.permutation(X.shape[0])
    indices = indices[:n_samples]
    XX = X[indices,:]
    yy = y[indices]
    return XX, yy

