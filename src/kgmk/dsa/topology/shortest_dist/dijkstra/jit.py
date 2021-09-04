import numpy as np 
import numba as nb 
import heapq



@nb.njit(
  (nb.i8, nb.i8[:, :], nb.i8),
  cache=True,
) 
def shortest_dist_dijkstra(
  n: int,
  csgraph: np.ndarray,
  src: int,
) -> np.ndarray:
  assert csgraph.shape == (len(csgraph), 3)
  inf = 1 << 60
  assert inf > csgraph[:, 2].max() * n
  sort_idx = np.argsort(csgraph[:, 0], kind='mergesort')
  csgraph = csgraph[sort_idx]
  edge_idx = np.searchsorted(csgraph[:, 0], np.arange(n + 1))
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  hq = [(0, src)]
  while hq:
    du, u = heapq.heappop(hq)
    if du > dist[u]: continue
    for i in range(edge_idx[u], edge_idx[u + 1]):
      _, v, w = csgraph[i]
      dv = du + w 
      if dv >= dist[v]: continue
      dist[v] = dv
      heapq.heappush(hq, (dv, v))
  return dist