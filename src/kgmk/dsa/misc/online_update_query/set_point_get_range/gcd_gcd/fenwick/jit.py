from kgmk.dsa.math.gcd.non_recursive.jit import (
  gcd,
)

# TODO cut below 
import numba as nb 


@nb.njit
def fw_op(a: int, b: int) -> int: return gcd(a, b)

@nb.njit 
def fw_e() -> int: return 0
