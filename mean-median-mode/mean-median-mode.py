from collections import Counter
import numpy as np
from scipy import stats

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mode_res = stats.mode(x, keepdims=False)

    return {
              "mean": float(np.mean(x)),
              "median": float(np.median(x)),
              "mode": float(mode_res.mode),
          }
    