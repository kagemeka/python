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

  mst = np.zeros((n - 1, 3), np.int64)
  mst_idx = 0
  def add_edge(u, v, w):
    nonlocal mst, mst_idx
    mst[mst_idx] = (u, v, w)
    mst_idx += 1
  
  uf = uf_build(n)
  root = np.arange(n)
    
  def update_all_root():
    nonlocal uf, n, root
    for i in range(n):
      root[i] = uf_find(uf, i)

  def all_same():
    nonlocal root
    return np.all(root == root[0])

  min_edge = np.zeros((n, 3), np.int64)

  while not all_same():
    min_edge[:, 2] = inf
    for i in range(m):
      u, v, w = csgraph[i]
      if root[u] == root[v]: continue
      if w < min_edge[root[u], 2]:
        min_edge[root[u]] = (u, v, w)
      if w < min_edge[root[v], 2]:
        min_edge[root[v]] = (v, u, w)
    for i in range(n):
      if i != root[i]: continue
      u, v, w = min_edge[i]
      if uf_find(uf, u) == uf_find(uf, v): continue
      uf_unite(uf, u, v)
      add_edge(u, v, w)
    update_all_root()
  return mst