import numpy as np 
import numba as nb



@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def to_undirected(
  g: np.ndarray,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, 3)
  g = np.vstack((g, g))
  g[n:, :2] = g[n:, 1::-1]
  return g  




@nb.njit(
  (nb.i8[:, :], nb.i8),
  cache=True,
)
def dense(
  g: np.ndarray,
  n: int,
) -> np.ndarray:
  m = len(g)
  assert g.shape == (m, 3)
  inf = 1 << 60
  a = np.full((n, n), inf, np.int64)
  for i in range(n): a[i, i] = 0
  for i in range(m):
    u, v, w = g[i]
    a[u, v] = a[v, u] = w 
  return a 