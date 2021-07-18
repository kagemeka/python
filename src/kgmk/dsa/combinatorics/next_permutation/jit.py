import numpy as np
import numba as nb



@nb.njit
def next_permutation(
  a: np.array,
) -> np.array:
  n = a.size
  i = -1
  for j in range(n - 1, 0, -1):
    if a[j - 1] >= a[j]:
      continue
    i = j - 1
    break
  if i == -1: 
    a[:] = -1; return a
  a[i + 1:] = a[i + 1:][::-1]
  for j in range(i + 1, n):
    if a[i] >= a[j]: continue
    a[i], a[j] = a[j], a[i]
    break
  return a