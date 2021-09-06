import numpy as np
import numba as nb


@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def csgraph_to_undirected(
  csgraph: np.ndarray,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  csgraph = np.vstack((csgraph, csgraph))
  csgraph[m:, :2] = csgraph[m:, 1::-1]
  return csgraph 