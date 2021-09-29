import numpy as np
import numba as nb



@nb.njit((nb.i8, nb.i8, nb.i8, nb.i8[:], nb.i8[:]), cache=True)
def mod_choose(
  n: int,
  k: int,
  mod: int,
  fact: np.ndarray,
  ifact: np.ndarray,
) -> int:
  ok = (0 <= k) & (k <= n)
  return fact[n] * ifact[n - k] % mod * ifact[k] % mod * ok


@nb.njit((nb.i8, nb.i8, nb.i8, nb.i8[:], nb.i8[:]), cache=True)
def mod_choose_inverse(
  n: int,
  k: int,
  mod: int,
  fact: np.ndarray,
  ifact: np.ndarray,
) -> int:
  ok = (0 <= k) & (k <= n)
  return ifact[n] * fact[n - k] % mod * fact[k] % mod * ok
  

@nb.njit((nb.i8, nb.i8, nb.i8, nb.i8[:], nb.i8[:]), cache=True)
def mod_nHk(
  n: int,
  k: int,
  mod: int,
  fact: np.ndarray,
  ifact: np.ndarray,
) -> int:
  return mod_choose(n + k - 1, k, mod, fact, ifact)