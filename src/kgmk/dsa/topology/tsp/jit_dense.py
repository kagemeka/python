import numpy as np
import numba as nb 



@nb.njit(
  (nb.i8[:, :], nb.i8),
  cache=True,
) 
def tsp(
  weights: np.ndarray,
  src: int,
) -> int:
  n = len(weights)
  assert weights.shape == (n, n)
  inf = 1 << 60
  assert inf > weights.sum()
  dist = np.full((1 << n, n), inf, np.int64)
  dist[1 << src, src] = 0 
  for s in range(1 << n):
    for i in range(n):
      if ~s >> i & 1: continue
      for j in range(n):
        if s >> j & 1: continue
        u = s | 1 << j 
        dist[u, j] = min(
          dist[u, j], 
          dist[s, i] + weights[i, j],
        )
  return np.amin(dist[-1] + weights[:, src])