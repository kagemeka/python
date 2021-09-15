import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def csgraph_to_undirected(g: np.ndarray) -> np.ndarray:
  m = len(g)
  g = np.vstack((g, g))
  g[m:, :2] = g[m:, 1::-1]
  return g