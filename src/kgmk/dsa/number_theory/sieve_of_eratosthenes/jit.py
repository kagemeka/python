import numpy as np 
import numba as nb


@nb.njit
def lpf(
  n: int = 1 << 20,
) -> np.array:
  s = np.arange(n)
  s[:2] = -1
  i = 0
  while i * i < n:
    i += 1
    if s[i] != i: continue
    s[i * 2::i] = i
  return s
  
  
@nb.njit
def spf(
  n: int = 1 << 20,
) -> np.array:
  s = np.arange(n)
  s[:2] = -1
  i = 0
  while i * i < n:
    i += 1
    if s[i] != i: continue
    for j in range(
      i * 2,
      n,
      i,
    ):
      if s[j] == j: s[j] = i
  return s


@nb.njit
def sieve_of_eratosthenes(
  n: int = 1 << 20,
) -> np.array:
  return lpf(n) == np.arange(n)