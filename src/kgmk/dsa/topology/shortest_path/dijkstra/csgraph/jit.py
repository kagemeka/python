import typing 
import numpy as np 
import numba as nb 
import heapq



@nb.njit
def shortest_path_dijkstra(
  n: int,
  g: np.ndarray,
  src: int,
) -> typing.Tuple[np.ndarray, np.ndarray]:
  assert g.shape == (len(g), 3)
  inf = 1 << 60
  assert inf > g[:, 2].max() * n
  g = g[np.argsort(g[:, 0], kind='mergesort')]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  predecessor = np.full(n, -1, np.int64)
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  hq = [(0, src)]
  while hq:
    du, u = heapq.heappop(hq) 
    if du > dist[u]: continue
    for i in range(edge_idx[u], edge_idx[u + 1]):
      _, v, w = g[i]
      dv = du + w 
      if dv >= dist[v]: continue
      dist[v] = dv
      predecessor[v] = u
      heapq.heappush(hq, (dv, v))
  return dist, predecessor