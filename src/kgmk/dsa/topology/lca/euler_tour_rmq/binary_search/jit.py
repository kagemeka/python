from \
  kgmk.dsa.tree.misc.segment.normal.one_indexed.bottomup \
  .jit \
import (
  seg_max_right,
)
from kgmk.dsa.topology.euler_tour.non_recursive.jit import (
  euler_tour,
)
from \
  kgmk.dsa.misc.online_update_query.set_point_get_range \
  .update_min.segtree.jit \
import (
  seg_e,
  seg_op,
  build_seg,
  get_range_seg,
)


# TODO cut below 


import numpy as np 
import numba as nb 


@nb.njit 
def lca_preprocess(
  n: int,
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> np.ndarray:
  tour, parent, depth = euler_tour(g, edge_idx, root)
  for i in range(n * 2):
    if tour[i] < 0: tour[i] = parent[~tour[i]]
  tour = tour[:-1]
  first_idx = np.full(n, -1, np.int32)
  for i in range(n * 2 - 1):
    u = tour[i]
    if first_idx[u] != -1: continue
    first_idx[u] = i
  seg = build_seg(depth[tour])
  return tour, first_idx, seg
 


@nb.njit 
def lca(
  tour: np.ndarray,
  first_idx: np.ndarray,
  seg: np.ndarray,
  u: int,
  v: int,
) -> int:
  l, r = first_idx[u], first_idx[v]
  if l > r: l, r = r, l
  mn = get_range_seg(seg, l, r + 1)
  is_ok = lambda x, mn: x > mn
  size = len(tour)
  i = seg_max_right(seg, seg_op, seg_e, is_ok, mn, l, size)
  return tour[i]
