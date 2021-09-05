from ....graph.jit.dense_graph_to_undirected import (
  dense_graph_to_undirected,
)

# TODO cut below

import numpy as np
import numba as nb


@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def mst_prim_dense(
  g: np.ndarray,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  inf = 1 << 60
  assert g.max() <= inf
  g = dense_graph_to_undirected(g)
  mst = np.zeros((n, 3), np.int64)
  mst_idx = -1
  def add_edge(u, v, w):
    nonlocal mst, mst_idx 
    mst[mst_idx] = (u, v, w)
    mst_idx += 1

  min_edge = np.full((n, 2), -1, np.int64)
  min_edge[:, 1] = inf
  min_edge[0, 1] = 0
  visited = np.zeros(n, np.bool8)
  for _ in range(n):
    pre, u, wu = -1, -1, inf
    for i in range(n):
      if visited[i]: continue
      p, w = min_edge[i]
      if w >= wu: continue
      pre, u, wu = p, i, w
    assert wu < inf
    add_edge(pre, u, wu)
    visited[u] = True
    for v in range(n):
      if visited[v]: continue
      if g[u, v] < min_edge[v, 1]:
        min_edge[v] = (u, g[u, v])
  mst = mst[:mst_idx]
  assert mst[:, 2].sum() == min_edge[:, 1].sum()
  return mst