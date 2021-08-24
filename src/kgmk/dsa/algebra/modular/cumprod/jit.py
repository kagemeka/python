import numpy as np
import numba as nb




@nb.njit
def mod_cumprod(
  a: np.array,
  mod: int,
) -> np.array:
  n = a.shape[0]
  for i in range(n - 1):
    a[i + 1] *= a[i]
    a[i + 1] %= mod