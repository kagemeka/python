import numpy as np 
import numba as nb



@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def floyd_warshall(
  g: np.ndarray,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  dist = g.copy()
  for k in range(n):
    for i in range(n):
      for j in range(n):
        dist[i, j] = min(
          dist[i, j],
          dist[i, k] + dist[k, j],
        )
  return dist 