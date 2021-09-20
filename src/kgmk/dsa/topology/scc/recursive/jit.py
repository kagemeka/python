from kgmk.dsa.topology.graph.jit.sort_csgraph import (
  sort_csgraph,
)

# TODO cut below
import numpy as np 
import numba as nb 


@nb.njit 
def _scc_dfs(n, g, edge_idx, que, visited, u):
  if visited[u]: return 
  visited[u] = True
  for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
    _scc_dfs(n, g, edge_idx, que, visited, v)
  que.append(u)


@nb.njit
def _scc_reverse_dfs(n, g, edge_idx, label, l, u):
  if label[u] != -1: return
  label[u] = l
  for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
    _scc_reverse_dfs(n, g, edge_idx, label, l, v)


@nb.njit
def scc(n: int, g: np.ndarray) -> np.ndarray:
  g = g.copy()
  g, edge_idx, _ = sort_csgraph(n, g)
  visited = np.zeros(n, np.bool8)
  que = [0] * 0
  for i in range(n):
    _scc_dfs(n, g, edge_idx, que, visited, 0)
  g[:, :2] = g[:, 1::-1]
  g, edge_idx, _ = sort_csgraph(n, g)    
  label = np.full(n, -1, np.int64)
  l = 0
  for i in que[::-1]:
    if label[i] != -1: continue
    _scc_reverse_dfs(n, g, edge_idx, label, l, i)
    l += 1
  return label
