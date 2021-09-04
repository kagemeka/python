import numpy as np
import numba as nb


@nb.njit(
  (nb.i8[:, :], nb.i8),
  cache=True,
)
def csgraph_to_dense(
  csgraph: np.ndarray,
  n: int,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  g = np.zeros((n, n), np.int64)
  for i in range(m):
    u, v, w = csgraph[i]
    g[u, v] = g[v, u] = w 
  return g 
