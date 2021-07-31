import numpy as np 
import numba as nb


@nb.njit
def bit_count(
  n: int,
) -> np.array:
  a = np.zeros(n, np.int64)
  for i in range(n):
    a[i] = a[i // 2] + i % 2
  return a