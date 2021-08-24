from ..cumprod.jit import (
  mod_cumprod,
)
from ..pow.jit import (
  mod_pow,
)


#TODO cut below

import numpy as np
import numba as nb


@nb.njit
def mod_factorial(
  n: int,
  mod: int,
) -> np.array:
  a = np.arange(n)
  a[0] = 1
  mod_cumprod(a, mod)
  return a


@nb.njit
def inv_mod_factorial(
  n: int,
  mod: int,
) -> np.array: 
  x = mod_factorial(n, mod)[-1]
  a = np.arange(1, n + 1)
  a[-1] = mod_pow(x, mod - 2, mod)
  mod_cumprod(a[::-1], mod)
  return a