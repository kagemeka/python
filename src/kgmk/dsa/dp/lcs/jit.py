import numpy as np
import numba as nb


@nb.njit
def lcs(
  a: np.array,
  b: np.array,
) -> np.array:
  n, m = a.size, b.size
  l = np.zeros(
    (n + 1, m + 1),
    dtype=np.int64,
  )
  for i in range(n):
    x = a[i]
    for j in range(m):
      l[i + 1][j + 1] = max(
        l[i][j + 1],
        l[i + 1][j],
        l[i][j] + (b[j] == x)
      )
  res = []
  i, j = n - 1, m - 1
  while i >= 0 and j >= 0:
    x = l[i + 1][j + 1]
    if l[i + 1][j] == x:
      j -= 1
      continue
    if l[i][j + 1] == x:
      i -= 1
      continue 
    res.append(a[i])
    i -= 1; j -= 1
  return np.array(res)[::-1]
