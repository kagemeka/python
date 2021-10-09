import typing 
import numpy as np 
import numba as nb



@nb.njit
def shortest_path_bellman_ford(
  n: int,
  g: np.ndarray,
  src: int,
) -> typing.Tuple[(np.ndarray, ) * 2]:
  m = len(g)
  assert g.shape == (m, 3)
  inf = 1 << 60
  assert inf > g[:, 2].max() * n
  predecessor = np.full(n, -1, np.int64)
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  for _ in range(n - 1):
    for i in range(m):
      u, v, w = g[i]
      if dist[u] + w >= dist[v]: continue
      dist[v] = dist[u] + w
      predecessor[v] = u
  for i in range(m):
    u, v, w = g[i]
    if dist[u] + w < dist[v]: 
      raise Exception('Negative cycle found.')
  return dist, predecessor