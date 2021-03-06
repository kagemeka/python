from ....graph.jit.csgraph_to_directed import (
  csgraph_to_directed,
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
  inf = 1 << 60
  assert csgraph[:, 2].max() < inf

  csgraph = csgraph_to_directed(csgraph)
  rev_edge_idx = np.zeros(m * 2, np.int64)
  rev_edge_idx[:m] = np.arange(m, 2 * m)
  rev_edge_idx[m:] = np.arange(m)
  m *= 2
  edge_idx = np.searchsorted(
    csgraph[:, 0][np.argsort(csgraph[:, 0])],
    np.arange(n + 1),
  )

  edge_is_added = np.zeros(m, np.bool8)
  added_edge_indices = np.full(m, -1, np.int64)
  idx_to_add_edge = edge_idx[:-1].copy()

  def add_edge(u, i):
    nonlocal added_edge_indices, idx_to_add_edge
    added_edge_indices[idx_to_add_edge[u]] = i
    idx_to_add_edge[u] += 1
    
  def label_nodes():
    nonlocal n, edge_idx, added_edge_indices, csgraph
    label = np.full(n, -1, np.int64)
    l = 0
    for i in range(n):
      if label[i] != -1: continue
      label[i] = l
      st = [i]
      while st:
        u = st.pop()
        for j in range(edge_idx[u], edge_idx[u + 1]):
          j = added_edge_indices[j]
          if j == -1: break
          v = csgraph[j, 1]
          if label[v] != -1: continue
          label[v] = l
          st.append(v)      
      l += 1
    return label  
  
  def update_min_edge_indices(label):
    nonlocal m, csgraph
    l = label.max()
    min_edge_idx = np.full(l + 1, -1, np.int64)
    for i in range(m):
      u, v, w = csgraph[i]
      u, v = label[u], label[v]
      if u == v: continue
      j = min_edge_idx[u]
      if j == -1 or w < csgraph[j, 2]:
        min_edge_idx[u] = i
      j = min_edge_idx[v]
      if j == -1 or w < csgraph[j, 2]:
        min_edge_idx[v] = rev_edge_idx[i]
      
    return min_edge_idx

  def add_min_edges(min_edge_idx):
    nonlocal rev_edge_idx, edge_is_added, csgraph
    for i in range(min_edge_idx.size):
      i = min_edge_idx[i]
      rev = rev_edge_idx[i]
      if edge_is_added[rev]: continue
      u, v, _ = csgraph[i]
      add_edge(u, i)
      add_edge(v, rev)
      edge_is_added[i] = True

  while 1:
    label = label_nodes()
    if label.max() == 0: break
    min_edge_idx = update_min_edge_indices(label)
    add_min_edges(min_edge_idx)

  added_edge_indices = np.flatnonzero(edge_is_added)
  assert added_edge_indices.size == n - 1
  return csgraph[added_edge_indices]