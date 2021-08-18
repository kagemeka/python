import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8[:]))
def kasai(
  a: np.array,
  sa: np.array,
) -> np.array:
  n = a.size
  assert n > 0 and sa.size == n
  rank = np.zeros(n, dtype=np.int64)
  rank[sa] = np.arange(n)
  h = np.zeros(n - 1, dtype=np.int64)
  l = 0
  for i in range(n):
    if l > 0: l -= 1
    r = rank[i]
    if r == n - 1: continue
    j = sa[r + 1]
    while i + l < n and j + l < n:
      if a[i + l] != a[j + l]: break 
      l += 1
    h[r] = l
  return h