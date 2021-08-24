import numpy as np
import numba as nb



@nb.njit
def mod_choose(
  n: int,
  k: int,
  mod: int,
  fact: np.array,
  ifact: np.array,
) -> int:
  ok = (0 <= k) & (k <= n)
  c = fact[n] * ifact[n - k] % mod * ifact[k] % mod
  return c * ok


@nb.njit
def inv_mod_choose(
  n: int,
  k: int,
  mod: int,
  fact: np.array,
  ifact: np.array,
) -> int:
  ok = (0 <= k) & (k <= n)
  c = ifact[n] * fact[n - k] % mod * fact[k] % mod
  return c * ok