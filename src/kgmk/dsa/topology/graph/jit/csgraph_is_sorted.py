import numpy as np 
import numba as nb


@nb.njit((nb.i8[:, :], ), cache=True)
def csgraph_is_sorted(csgraph: np.ndarray) -> bool:
  return np.all(csgraph[:-1, 0] <= csgraph[1:, 0])
