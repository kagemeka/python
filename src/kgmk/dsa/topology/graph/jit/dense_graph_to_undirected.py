import numpy as np
import numba as nb 



@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def dense_graph_to_undirected(
  g: np.ndarray,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  g = g.copy()
  for u in range(n):
    for v in range(n):
      g[v, u] = min(g[v, u], g[u, v])
  return g