import numpy as np 
import numba as nb


@nb.njit
def bit_count(n: int) -> np.ndarray:
  cnt = np.zeros(n, np.int64)
  for i in range(n): cnt[i] = cnt[i >> 1] + i & 1
  return cnt