import numpy as np

def norm_minmax(X, low=-1, high=1):
    assert low < high
    m1 = np.min(X)
    m2 = np.max(X)
    return (X-m1)/(m2 - m1) * (high-low) + low

def norm_zscore(X):
    mu = np.mean(X)
    sigma = np.std(X)
    return (X - mu)/sigma

