import numpy as np 
import numba as nb




@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def floyd_warshall(
  n: int,
  g: np.ndarray,
) -> np.ndarray:
  m = len(g)
  assert g.shape == (m, 3)
  inf = 1 << 60
  dist = np.full((n, n), inf, np.int64)
  for i in range(n): dist[i, i] = 0
  for i in range(m):
    u, v, w = g[i]
    dist[u, v] = min(dist[u, v], w)
  for k in range(n):
    for i in range(n):
      for j in range(n):
        dist[i, j] = min(
          dist[i, j],
          dist[i, k] + dist[k, j],
        )
  return dist 