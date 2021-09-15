from kgmk.dsa.algebra.modular.pow.non_recursive.jit import (
  mod_pow,
)

# TODO cut below

import numba as nb 


@nb.njit
def mod_inverse(a: int, p: int) -> int:
  return mod_pow(a, p - 2, p)
  