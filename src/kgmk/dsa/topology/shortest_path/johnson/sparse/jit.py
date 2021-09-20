from kgmk.dsa.topology.shortest_path.dijkstra.csgraph.jit \
import (
  shortest_path_dijkstra,
)
from kgmk.dsa.topology.shortest_path.bellman_ford.csgraph.jit \
import (
  shotest_path_bellman_ford,
)


# TODO cut below 

import numpy as np 
import numba as nb 


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def shotest_dist_johnson(
  n: int,
  csgraph: np.ndarray,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  new_edges = np.zeros((n, 3), np.int64)
  new_edges[:, 0] = n
  new_edges[:, 1] = np.arange(n)
  csgraph = np.vstack((csgraph, new_edges))
  h, _ = shotest_path_bellman_ford(n + 1, csgraph, n)[:-1]
  csgraph = csgraph[:m]
  csgraph[:, 2] += h[csgraph[:, 0]] - h[csgraph[:, 1]]
  dist = np.zeros((n, n), np.int64)
  for i in range(n):
    d, _ = shortest_path_dijkstra(n, csgraph, i)
    dist[i] = d - h[i] + h  
  return dist