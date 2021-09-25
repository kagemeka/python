import numpy as np 
import numba as nb

@nb.njit
def digits_to_int(digits: np.ndarray) -> int:
  x = 0
  for d in digits[::-1]:
    x = x * 10 + d
  return x 