import numpy as np
import numba as nb



@nb.njit
def lcp_kasai(
  a: np.ndarray,
  sa: np.ndarray,
) -> np.ndarray:
  n = a.size
  assert n > 0 and sa.size == n
  
  rank = np.empty(n, np.int32)
  for i in range(n): rank[sa[i]] = i
  h, l = np.empty(n - 1, np.int32), 0
  for i in range(n):
    if l: l -= 1
    r = rank[i]
    if r == n - 1: continue
    j = sa[r + 1]
    while i + l < n and j + l < n:
      if a[i + l] != a[j + l]: break 
      l += 1
    h[r] = l
  return h