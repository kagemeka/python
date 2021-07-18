from \
  ..sieve_of_eratosthenes.jit \
import (
  sieve_of_eratosthenes,
)
# TODO cut below


import numpy as np 
import numba as nb


@nb.njit
def prime_numbers(
  n: int = 1 << 20,
) -> np.array:
  a = sieve_of_eratosthenes(n)
  return np.flatnonzero(a)