import numpy as np 
import numba as nb 


@nb.njit 
def maximum_flow_edmonds_karp(
  g: np.ndarray,
  src: int,
  sink: int,
) -> int:
  n = len(g)
  inf = 1 << 60
  g = g.copy()
  prev = np.empty(n, np.int64)
  level = np.empty(n, np.int64)

  def find_path():
    prev[:] = -1
    level[:] = -1
    level[src] = 0
    fifo_que = [src]
    for u in fifo_que:
      if u == sink: return
      for v in range(n):
        if g[u, v] == 0 or level[v] != -1: continue
        level[v] = level[u] + 1
        prev[v] = u
        fifo_que.append(v)
      
  def augment_flow():
    v = sink
    flow = inf
    while prev[v] != -1:
      u = prev[v]
      flow = min(flow, g[u, v])
      v = u
    if flow == inf: return 0
    v = sink 
    while prev[v] != -1:
      u = prev[v]
      g[u, v] -= flow
      g[v, u] += flow
      v = u
    return flow

  flow = 0 
  while 1:
    find_path()
    f = augment_flow()
    if not f: return flow
    flow += f