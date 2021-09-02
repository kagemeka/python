import heapq 
import numpy as np 
import numba as nb 



@nb.njit(
  (nb.i8, nb.i8[:, :], nb.i8),
  cache=True,
)
def shortest_dist_dijkstra(
  n: int,
  edges: np.ndarray,
  src: int,
) -> np.ndarray:
  inf = 1 << 60
  edges = edges[np.argsort(edges[:, 0], kind='mergesort')]
  idx = np.searchsorted(edges[:, 0], np.arange(n + 1)) 
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  hq = [(0, src)]
  while hq:
    du, u = heapq.heappop(hq)
    if du > dist[u]: continue
    for edge_idx in range(idx[u], idx[u + 1]):
      _, v, w = edges[edge_idx]
      dv = du + w
      if dv >= dist[v]: continue
      dist[v] = dv 
      heapq.heappush(hq, (dv, v))
  return dist