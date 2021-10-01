import numpy as np 
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def shortest_dist_floyd_warshall(g: np.ndarray) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  g = g.copy()
  for i in range(n): g[i, i] = 0
  for k in range(n):
    for i in range(n):
      for j in range(n):
        g[i, j] = min(g[i, j], g[i, k] + g[k, j])
  return g