from ...union_find.parent_size_at_same.jit import (
  uf_unite,
  uf_build,
  uf_find,
)

# TODO cut below

import numpy as np
import numba as nb



@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def mst_kruskal(
  n: int,
  csgraph: np.ndarray,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  sort_idx = np.argsort(csgraph[:, 2], kind='mergesort')
  csgraph = csgraph[sort_idx]
  uf = uf_build(n)

  edge_indices = np.zeros(m, np.int64)
  j = 0

  def add_edge(i):
    nonlocal edge_indices, j
    edge_indices[j] = i
    j += 1

  for i in range(m):
    u, v, _ = csgraph[i]
    if uf_find(uf, u) == uf_find(uf, v): continue
    uf_unite(uf, u, v)
    add_edge(i)

  return csgraph[edge_indices[:j]]