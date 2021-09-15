import numpy as np 
import numba as nb 


@nb.njit((nb.i8, nb.i8), cache=True)
def mod_fibonacci_sequence(n: int, mod: int) -> np.ndarray:
  assert n >= 2
  f = np.empty(n, np.int64)
  f[0], f[1] = 0, 1
  for i in range(2, n):
    f[i] = (f[i - 1] + f[i - 2]) % mod 
  return f 