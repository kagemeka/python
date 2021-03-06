from kgmk.dsa.topology.graph.jit.csgraph_is_sorted import (
  csgraph_is_sorted,
)


import numpy as np 
import numba as nb 


@nb.njit((nb.i8, nb.i8[:, :], nb.i8[:], nb.i8), cache=True)
def graph_bfs(
  n: int, 
  g: np.ndarray,
  edge_idx: np.ndarray,
  src: int,
) -> np.ndarray:
  assert csgraph_is_sorted(g)
  level = np.full(n, -1, np.int64)
  level[src] = 0
  que = [src]
  for u in que:
    for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
      if level[v] != -1: continue
      level[v] = level[u] + 1
      que.append(v)
  return level