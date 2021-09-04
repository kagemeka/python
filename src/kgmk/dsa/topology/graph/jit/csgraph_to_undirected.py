import numpy as np
import numba as nb


@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def csgraph_to_undirected(
  g: np.ndarray,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, 3)
  g = np.vstack((g, g))
  g[n:, :2] = g[n:, 1::-1]
  return g  
