from kgmk.dsa.math.extended_gcd.recursive.jit import (
  ext_gcd,
)

# TODO cut below 
import numba as nb 


@nb.njit((nb.i8, nb.i8), cache=True)
def mod_inv(a: int, mod: int) -> int:
  g, p, q = ext_gcd(a, mod)
  if g != 1:
    raise ArithmeticError(
      'modular multiplicative inverse does not exist.'
    )
  return p % mod