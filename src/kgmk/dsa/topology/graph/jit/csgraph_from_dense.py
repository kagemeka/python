import numpy as np
import numba as nb


@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def csgraph_from_dense(
  g: np.ndarray,
) -> np.ndarray:
  inf = 1 << 60
  n = len(g)
  assert g.shape == (n, n)
  exist_edge = g != inf
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