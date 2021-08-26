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
  x = np.eye(
    a.shape[0],
    dtype=np.int64,
  )
  while n:
    if n & 1:
      x = mod_matrix_dot(x, a, mod)
    x = mod_matrix_dot(x, x, mod)
    n >>= 1
  return x