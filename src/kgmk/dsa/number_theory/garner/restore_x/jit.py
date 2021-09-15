from kgmk.dsa.algebra.modular.inverse.ext_gcd.jit import (
  mod_inv,
)

# TODO cut below 

import numpy as np
import numba as nb 


@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def garner(
  r: np.ndarray,
  m: np.ndarray,
) -> int:
  n = r.size 
  assert m.size == n
  x = 0
  m_prod = 1
  for i in range(n):
    t = (r[i] - x) * mod_inv(m_prod, m[i]) % m[i]
    x += t * m_prod
    m_prod *= m[i]
  return x
    