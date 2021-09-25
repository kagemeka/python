from kgmk.dsa.algebra.modular.pow.non_recursive.jit import (
  mod_pow,
)

# TODO cut below

import numba as nb 


@nb.njit 
def mod_inverse(n: int, p: int) -> int:
  return mod_pow(n, p - 2, p)
  