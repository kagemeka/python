# TODO cut below
import numpy as np 
import numba as nb 


@nb.njit 
def mod_pow2_inverse(n: int, p: int) -> np.ndarray:
  inv_2 = (p + 1) // 2
  a = np.ones(n, np.int64)
  for i in range(n - 1): a[i + 1] = a[i] * inv_2 % p
  return a