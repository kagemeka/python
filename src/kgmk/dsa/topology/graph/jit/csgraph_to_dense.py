import numpy as np
import numba as nb


@nb.njit 
def csgraph_to_dense(n: int, g: np.ndarray) -> np.ndarray:
  inf = 1 << 60
  m = len(g)
  assert g.shape == (m, 3)
  t = np.full((n, n), inf, np.int64)
  for i in range(m):
    u, v, w = g[i]
    t[u, v] = w
  return t 