import numpy as np 
import numba as nb
import heapq



@nb.njit((nb.i8[:, :], nb.i8), cache=True)
def shortest_path_dijkstra(
  g: np.ndarray,
  src: int,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  inf = 1 << 60
  assert g.max() <= inf
  predecessor = np.full(n, -1, np.int64)
  dist = np.full(n, inf, np.int64)
  dist[src] = 0 
  hq = [(0, src)]
  while hq:
    du, u = heapq.heappop(hq)
    if du > dist[u]: continue
    for v in range(n):
      dv = du + g[u, v]
      if dv >= dist[v]: continue 
      dist[v] = dv
      predecessor[v] = u
      heapq.heappush(hq, (dv, v))
  return predecessor