import numpy as np


def sigmoid(x: list | float) -> np.ndarray | float:
  """
    Returns the sigmoid value for a scalar or each element of a list.
    """
  if x is None:
    return np.array([])

  if isinstance(x, (int, float)):
    return float(1 / (1 + np.exp(-x)))

  arr = np.asarray(x, dtype=float)
  return 1 / (1 + np.exp(-arr))
