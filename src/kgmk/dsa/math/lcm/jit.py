from ..gcd.non_recursive.jit import (
  gcd,
)

# TODO cut below 

import numba 


def lcm(a: int, b: int) -> int:
  return a // gcd(a, b) * b