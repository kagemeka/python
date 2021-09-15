from kgmk.dsa.topology.graph.jit.csgraph_to_undirected import (
  csgraph_to_undirected,
)
from kgmk.dsa.topology.graph.jit.sort_csgraph import (
  sort_csgraph,
)

# TODO cut below 


import numpy as np
import numba as nb 



@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def connected_components_bfs(n: int, g: np.ndarray):
  g = csgraph_to_undirected(g)
  g, edge_idx, _ = sort_csgraph(n, g)
  label = np.full(n, -1, np.int64)
  l = 0 
  for i in range(n):
    if label[i] != -1: continue
    label[i] = l
    que = [i]
    for u in que:
      for v in g[edge_idx[u]:edge_idx[u + 1], 1]:
        if label[v] != -1: continue
        label[v] = l
        que.append(v)
    l += 1
  return label