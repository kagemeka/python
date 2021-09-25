from ..cumprod.jit import (
  mod_cumprod,
)
from ..inverse.fermat.jit import (
  mod_inverse,
)


#TODO cut below

import numpy as np
import numba as nb


@nb.njit 
def mod_factorial(n: int, mod: int) -> np.ndarray:
  a = np.arange(n)
  a[0] = 1
  mod_cumprod(a, mod)
  return a


@nb.njit 
def mod_factorial_inverse(n: int, p: int) -> np.ndarray:
  a = np.arange(1, n + 1)
  a[-1] = mod_inverse(mod_factorial(n, p)[-1], p)
  mod_cumprod(a[::-1], p)
  return a