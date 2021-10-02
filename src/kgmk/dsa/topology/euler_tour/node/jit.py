from ..edge.non_recursive.jit import (
  euler_tour_edge,
)

# TODO cut below
import typing 
import numpy as np 
import numba as nb 


@nb.njit 
def euler_tour_node(
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> typing.Tuple[(np.ndarray, ) * 4]:
  tour, parent, depth = euler_tour_edge(g, edge_idx, root)
  n = len(tour) >> 1
  tour = tour[:-1]
  first_idx = np.full(n, -1, np.int64)
  for i in range(2 * n - 1):
    u = tour[i]
    if u < 0:
      tour[i] = parent[~u]
      continue
    first_idx[u] = i
  return tour, first_idx, parent, depth
