import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    '''
    x_sorted = sorted(x)
    n = len(x_sorted)
    result = []
    
    for p in q:
        # Find the fractional index
        idx = (p / 100) * (n - 1)
        lower = int(idx)
        upper = min(lower + 1, n - 1)
        weight = idx - lower
    
        # Linear interpolation between adjacent values
        val = x_sorted[lower] * (1 - weight) + x_sorted[upper] * weight
        result.append(val)
    
    return np.array(result)
    '''
    return np.percentile(x, q)