from kgmk.dsa.topology.graph.jit.sort_csgraph import (
  sort_csgraph,
)

# TODO cut below
import numpy as np 
import numba as nb 


@nb.njit
def scc(n: int, g: np.ndarray) -> np.ndarray:
  def _scc_dfs(n, g): 
    g, edge_idx, _ = sort_csgraph(n, g)
    que = np.empty(n, np.int64)
    ptr = -1 
    visited = np.zeros(n, np.bool8)
    for i in range(n):
      if visited[i]: continue
      st = [i]
      while st:
        u = st.pop()
        if u < 0:
          u = -u - 1
          que[ptr] = u
          ptr -= 1
          continue
        if visited[u]: continue
        visited[u] = True
        st.append(-u - 1)
        for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
          if visited[v]: continue
          st.append(v)
    return que

  def _scc_reverse_dfs(n, g, que):
    g[:, :2] = g[:, 1::-1]
    g, edge_idx, _ = sort_csgraph(n, g)
    label = np.full(n, -1, np.int64)
    l = 0
    for i in que:
      if label[i] != -1: continue
      st = [i]
      label[i] = l
      while st:
        u = st.pop()
        for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
          if label[v] != -1: continue
          label[v] = l
          st.append(v)
      l += 1
    return label
  
  g = g.copy()
  que = _scc_dfs(n, g)
  return _scc_reverse_dfs(n, g, que)