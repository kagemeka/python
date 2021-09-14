from kgmk.dsa.math.extended_gcd.recursive.jit import (
  ext_gcd,
)

# TODO cut below 

import typing
import numpy as np 
import numba as nb 



@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def crt(
  r: np.ndarray,
  m: np.ndarray,
) -> typing.Tuple[int, int]:
  r0, m0 = 0, 1
  assert r.size == m.size 
  for i in range(r.size):
    r1, m1 = r[i], m[i]
    d, p, q = ext_gcd(m0, m1)
    if (r1 - r0) % d: return 0, 0
    u1 = m1 // d 
    r0 += (r1 - r0) // d % u1 * p % u1 * m0
    m0 *= u1 
    r0 %= m0
  return r0, m0