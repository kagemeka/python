import numpy as np 
import typing
import numba as nb


@nb.njit
def sieve_of_eratosthenes(
  n: int = 1 << 20,
) -> np.array:
  s = np.ones(n, np.bool8)
  s[:2] = 0
  i = 0 
  while i * i < n:
    i += 1
    if not s[i]: continue
    s[i * 2::i] = 0
  return s