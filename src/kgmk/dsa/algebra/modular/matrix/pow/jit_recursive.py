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
  if n == 0:
    return np.eye(
      a.shape[0],
      dtype=np.int64,
    )  
  x = mod_matrix_pow(a, n >> 1, mod)
  x = mod_matrix_dot(x, x, mod)
  if n & 1: 
    x = mod_matrix_dot(x, a, mod)
  return x
