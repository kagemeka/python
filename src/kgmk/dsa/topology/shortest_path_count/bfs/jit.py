import typing 
import numpy as np
import numba as nb 



@nb.njit 
def shortest_path_cnt_bfs(
  n: int, 
  g: np.ndarray,
  edge_idx: np.ndarray,
  src: int,
  mod: int,
) -> typing.Tuple[np.ndarray, np.ndarray]:
  inf = 1 << 60
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  paths = np.zeros(n, np.int64)
  paths[src] = 1    
  fifo_que = [src]
  for u in fifo_que:
    for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
      dv = dist[u] + 1
      if dv > dist[v]: continue
      if dv == dist[v]:
        paths[v] += paths[u]
        paths[v] %= mod
        continue
      dist[v] = dv
      paths[v] = paths[u]
      fifo_que.append(v)
  return dist, paths