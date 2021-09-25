import numpy as np 
import numba as nb

@nb.njit
def int_to_digits(n: int) -> np.ndarray:
  digits = np.zeros(20, np.int64)
  i = 0
  while n:
    n, r = divmod(n, 10)
    digits[i] = r
    i += 1
  return digits[:i]

