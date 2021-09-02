import numpy as np 
import numba as nb



@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def floyd_warshall(
  g: np.ndarray,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  inf = 1 << 60
  assert inf > g.max() * n 
  dist = np.full((n, n), inf, np.int64)
  for i in range(n): dist[i, i] = 0
  for u in range(n):
    for v in range(n):
      if g[u, v] == 0: continue
      dist[u, v] = g[u, v]
  for k in range(n):
    for i in range(n):
      for j in range(n):
        dist[i, j] = min(
          dist[i, j],
          dist[i, k] + dist[k, j],
        )
  return dist 