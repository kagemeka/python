import typing
import numpy as np 
import numba as nb 
import heapq 


@nb.njit 
def shortest_path_cnt_dijkstra(
  n: int, 
  g: np.ndarray,
  src: int,
  mod: int,
) -> typing.Tuple[np.ndarray, np.ndarray]:
  inf = 1 << 60
  assert inf > g[:, 2].max() * n
  g = g[np.argsort(g[:, 0], kind='mergesort')]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  paths = np.zeros(n, np.int64)
  paths[src] = 1
  hq = [(0, src)]
  while hq:
    du, u = heapq.heappop(hq)
    if du > dist[u]: continue
    for i in range(edge_idx[u], edge_idx[u + 1]):
      _, v, w = g[i]
      dv = du + w
      if dv > dist[v]: continue
      if dv == dist[v]:
        paths[v] += paths[u]
        paths[v] %= mod
        continue
      dist[v] = dv
      paths[v] = paths[u]
      heapq.heappush(hq, (dv, v))
  return dist, paths