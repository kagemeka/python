from kgmk.dsa.math.extended_gcd.recursive.jit import (
  ext_gcd,
)

# TODO cut below 
import numba as nb 


@nb.njit
def mod_inv(a: int, mod: int) -> int:
  g, p, _ = ext_gcd(a, mod)
  if g == 1: return p % mod
  msg = 'Modular multiplicative inverse does not exist.'
  raise ArithmeticError(msg)
