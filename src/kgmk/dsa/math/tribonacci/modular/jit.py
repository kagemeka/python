
import numpy as np
import numba as nb 


@nb.njit
def mod_tribonacci_sequence(n: int, mod: int) -> np.ndarray:
  assert n >= 3
  t = np.zeros(n, np.int64)
  t[2] = 1
  for i in range(3, n):
    t[i] = (t[i - 1] + t[i - 2] + t[i - 3]) % mod 
  return t 