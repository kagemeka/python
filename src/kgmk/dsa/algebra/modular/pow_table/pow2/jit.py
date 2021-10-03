import numpy as np
import numba as nb


@nb.njit 
def mod_pow2(n: int, p: int) -> np.ndarray:
  a = np.ones(n, np.int64)
  for i in range(n - 1): a[i + 1] = a[i] * 2 % p
  return a