import numpy as np 
import numba as nb


@nb.njit((nb.i8[:, :], ), cache=True)
def csgraph_is_sorted(g: np.ndarray) -> bool:
  return np.all(g[:-1, 0] <= g[1:, 0])
