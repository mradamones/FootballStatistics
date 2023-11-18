import pandas as pd
import numpy as np


def standardize(array):
    array = array.apply(pd.to_numeric, errors='coerce')
    avg = np.mean(array, axis=0)
    std_dev = np.std(array, axis=0)
    standardized_array = (array - avg) / std_dev
    standardized_array = np.round(standardized_array, 3)
    return standardized_array


def min_max_normalize(array):
    array = array.apply(pd.to_numeric, errors='coerce')
    min_val = np.min(array, axis=0)
    max_val = np.max(array, axis=0)
    normalized_array = (array - min_val) / (max_val - min_val)
    normalized_array = np.round(normalized_array, 3)
    return normalized_array