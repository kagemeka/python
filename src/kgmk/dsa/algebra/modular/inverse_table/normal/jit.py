from kgmk.dsa.algebra.modular.factorial.jit import (
  mod_factorial,
  mod_factorial_inverse,
)


# TODO cut below

import numpy as np
import numba as nb


@nb.njit
def mod_inverse_table(n: int, mod: int) -> np.ndarray:
  a = mod_factorial_inverse(n, mod)
  a[1:] *= mod_factorial(n - 1, mod)
  return a