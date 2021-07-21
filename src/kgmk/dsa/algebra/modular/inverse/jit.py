from ..factorial.jit import (
  factorial,
  inv_factorial,
)


# TODO cut below

import numpy as np
import numba as nb


@nb.njit
def inverse(
  n: int,
  modulo: int,
) -> np.array:
  m = modulo
  a = inv_factorial(n, m)
  a[1:] *= factorial(n - 1, m)
  return a % m
