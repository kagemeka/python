from kgmk.dsa.algebra.modular.pow.non_recursive.jit import (
  mod_pow,
)
from kgmk.dsa.number_theory.euler_totient.naive.jit import (
  euler_totient,
)

# TODO cut below 
import numba as nb 


@nb.njit((nb.i8, nb.i8), cache=True)
def mod_inverse(a: int, n: int) -> int:
  phi = euler_totient(n)
  return mod_pow(a, phi - 1, n)