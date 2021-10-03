from kgmk.dsa.algebra.modular.pow.bottomup.jit import (
  mod_pow,
)
from kgmk.dsa.number_theory.euler_totient.naive.jit import (
  euler_totient,
)

# TODO cut below 
import numba as nb 


@nb.njit
def mod_inverse(a: int, n: int) -> int:
  return mod_pow(a, euler_totient(n) - 1, n)