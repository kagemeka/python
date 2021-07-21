from \
  kgmk.dsa.algebra.modular \
  .factorial.jit \
import (
  inv_factorial,
  cumprod,
)

# TODO cut below


import numba as nb
import numpy as np


@nb.njit
def nchoose(
  n: int,
  rmax: int,
  modulo: int,
) -> int:
  r, m = rmax, modulo
  a = np.arange(
    n + 1,
    n - r,
    -1,
  ); a[0] = 1
  cumprod(a, m)
  a *= inv_factorial(r + 1, m)
  return a % m
  