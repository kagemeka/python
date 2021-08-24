mod: int
fact: np.array
ifact: np.array


# TODO cut below

import numpy as np
import numba as nb



def mod_choose(n, k):
  ok = (0 <= k) & (k <= n)
  c = fact[n] * ifact[n - k] % mod * ifact[k] % mod
  return c * ok


def inv_mod_choose(n, k):
  ok = (0 <= k) & (k <= n)
  c = ifact[n] * fact[n - k] % mod * fact[k] % mod
  return c * ok