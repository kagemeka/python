from kgmk.dsa.topology.graph.jit.csgraph_is_sorted import (
  csgraph_is_sorted,
)


# TODO cut below 

import numpy as np
import numba as nb 


@nb.njit((nb.i8, nb.i8[:, :], nb.i8[:], nb.i8), cache=True) 
def shortest_dist_bfs(
  n: int,
  csgraph: np.ndarray,
  edge_idx: np.ndarray,
  src: int,
) -> np.ndarray:
  assert csgraph.shape == (len(csgraph), 2)
  inf = 1 << 60
  assert csgraph_is_sorted(csgraph)
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  fifo_q = [0]
  for u in fifo_q:
    for i in range(edge_idx[u], edge_idx[u + 1]):
      v = csgraph[i, 1]
      dv = dist[u] + 1
      if dv >= dist[v]: continue
      dist[v] = dv
      fifo_q.append(v)
  return dist