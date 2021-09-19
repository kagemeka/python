from kgmk.dsa.topology.tree_bfs.jit import (
  tree_bfs,
)

# TODO cut below

import numpy as np 
import numba as nb 


@nb.njit((nb.i8[:, :], nb.i8), cache=True)
def tree_diameter(g: np.ndarray, edge_idx: np.ndarray) -> int:
  _, depth = tree_bfs(g, edge_idx, 0)
  root = np.argmax(depth)
  _, depth = tree_bfs(g, edge_idx, root)
  return depth.max()