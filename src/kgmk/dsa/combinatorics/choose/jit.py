import numpy as np
mod: int
fact: np.array
ifact: np.array

# this function cannot used via importing.
# it's need to copy and paste it into other sources.
# TODO cut below


import numba as nb


@nb.njit
def choose(
  n: int,
  r: int,
) -> int:
  global mod, fact, ifact
  ok = (0 <= r) & (r <= n)
  c = fact[n] * ok
  c = c * ifact[n - r] % mod
  return c * ifact[r] % mod