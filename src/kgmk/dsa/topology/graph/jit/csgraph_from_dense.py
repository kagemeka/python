import numpy as np
import numba as nb


@nb.njit(
  (nb.i8[:, :], nb.b1),
  cache=True,
)
def csgraph_from_dense(
  g: np.ndarray,
  zero_is_null: bool=True,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  exist_edge = np.full_like(g, 1, np.bool8)
  if zero_is_null:
    exist_edge &= g != 0
  m = exist_edge.sum()
  csgraph = np.zeros((m, 3), np.int64)
  k = 0  
  def add_edge(u, v, w):
    nonlocal csgraph, k 
    csgraph[k] = (u, v, w)
    k += 1
  for i in range(n):
    for j in range(n):
      if not exist_edge[i, j]: continue
      add_edge(i, j, g[i, j])
  return csgraph
