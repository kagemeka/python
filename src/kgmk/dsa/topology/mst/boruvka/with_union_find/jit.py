from ....union_find.parent_size_at_same.jit import (
  uf_build,
  uf_find,
  uf_unite,
)


# TODO cut below 

import numpy as np 
import numba as nb


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def mst_boruvka(
  n: int,
  csgraph: np.ndarray,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  inf = 1  << 60
  assert csgraph[:, 2].max() < inf
  edge_is_added = np.zeros(m, np.bool8)
  min_edge_idx = np.zeros(n, np.int64)
  uf = uf_build(n)
  root = np.arange(n)
    
  def update_all_roots():
    nonlocal uf, n, root
    for i in range(n):
      root[i] = uf_find(uf, i)

  def all_same():
    nonlocal root
    return np.all(root == root[0])

  def update_min_edge_indices():
    nonlocal min_edge_idx, m, csgraph, root
    min_edge_idx[:] = -1
    for i in range(m):
      u, v, w = csgraph[i]
      u, v = root[u], root[v]
      if u == v: continue
      j = min_edge_idx[u]
      if j == -1 or w < csgraph[j, 2]:
        min_edge_idx[u] = i
      j = min_edge_idx[v]
      if j == -1 or w < csgraph[j, 2]:
        min_edge_idx[v] = i

  def add_min_edges():
    nonlocal n, root, min_edge_idx, csgraph, uf
    for i in range(n):
      if i != root[i]: continue
      i = min_edge_idx[i]
      if edge_is_added[i]: continue
      u, v, _ = csgraph[i]
      uf_unite(uf, u, v)
      edge_is_added[i] = True

  while not all_same():
    update_min_edge_indices()
    add_min_edges()
    update_all_roots()

  added_edge_indices = np.flatnonzero(edge_is_added)
  assert added_edge_indices.size == n - 1
  return csgraph[added_edge_indices]