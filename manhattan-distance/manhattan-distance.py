import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # sum =0
    # for i in range(0,len(x)):
    #     sum += abs(x[i] - y[i])
    # return float(sum)

    ## optimized version
    x_arr = np.asarray(x) # convert in to numpy array
    y_arr = np.asarray(y)
    return float(np.sum(np.abs(x_arr - y_arr)))