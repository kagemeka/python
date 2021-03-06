import numpy as np 
import numba as nb 


@nb.njit 
def maximum_flow_ford_fulkerson(
  g: np.ndarray,
  src: int,
  sink: int,
) -> int:
  n = len(g)
  inf = 1 << 60
  g = g.copy()
  prev = np.empty(n, np.int64)
  visited = np.zeros(n, np.bool8)

  def find_path():
    prev[:] = -1
    visited[:] = False
    st = [src]
    while st:
      u = st.pop()
      if u == sink: return
      if visited[u]: continue
      visited[u] = True
      for v in range(n - 1, -1, -1):
        if g[u, v] == 0 or visited[v]: continue
        prev[v] = u
        st.append(v)
      
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