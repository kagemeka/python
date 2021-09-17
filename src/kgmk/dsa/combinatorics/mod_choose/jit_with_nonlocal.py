from kgmk.dsa.algebra.modular.factorial.jit import (
  mod_factorial,
  mod_factorial_inverse,
)


# TODO cut below

import numpy as np
import numba as nb


@nb.njit(cache=True)
def solve():
  mod = 10 ** 9 + 7
  n = 100
  fact = mod_factorial(n, mod)
  ifact = mod_factorial_inverse(n, mod)
  

  def mod_choose(n, k):
    nonlocal mod, fact, ifact
    ok = (0 <= k) & (k <= n)
    return fact[n] * ifact[k] % mod * ifact[n - k] % mod * ok


  def mod_choose_inverse(n, k):
    nonlocal mod, fact, ifact
    ok = (0 <= k) & (k <= n)
    return ifact[n] * fact[n - k] % mod * fact[k] % mod * ok


  def mod_nHk(n, k):
    return mod_choose(n + k - 1, k)