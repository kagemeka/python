import numpy as np 
import numba as nb



@nb.njit(
  (nb.i8, nb.i8[:, :], nb.i8),
  cache=True,
)
def shotest_dist_bellman_ford(
  n: int,
  csgraph: np.ndarray,
  src: int,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  inf = 1 << 60
  assert inf > csgraph[:, 2].max() * n
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  for _ in range(n - 1):
    for i in range(m):
      u, v, w = csgraph[i]
      dist[v] = min(dist[v], dist[u] + w)
  for i in range(m):
    u, v, w = csgraph[i]
    if dist[u] + w < dist[v]: 
      raise Exception('Negative cycle found.')
  return dist