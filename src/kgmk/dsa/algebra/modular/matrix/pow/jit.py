from ..dot.jit import (
  mod_matrix_dot,
)

# TODO cut below

import numpy as np
import numba as nb



@nb.njit
def mod_matrix_pow(
  a: np.ndarray,
  n: int,
  mod: int,
) -> np.ndarray:
  m = len(a)
  assert a.shape == (m, m)
  x = np.eye(m, dtype=np.int64)
  while n:
    if n & 1:
      x = mod_matrix_dot(x, a, mod)
    a = mod_matrix_dot(a, a, mod)
    n >>= 1
  return x