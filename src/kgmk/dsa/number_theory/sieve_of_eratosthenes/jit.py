import numpy as np 
import numba as nb



@nb.njit
def sieve_of_eratosthenes(n: int=1 << 20) -> np.array:
  return gpf(n) == np.arange(n)


@nb.njit
def gpf(n: int=1 << 20) -> np.array:
  s = np.arange(n)
  s[:2] = -1
  i = 0 
  while i * i < n - 1:
    i += 1
    if s[i] == i: s[i::i] = i
  return s


@nb.njit
def lpf(n: int=1 << 20) -> np.array:
  s = np.arange(n)
  s[:2] = -1
  i = 0 
  while i * i < n - 1:
    i += 1
    if s[i] != i: continue
    j = np.arange(i, n, i)
    s[j[s[j] == j]] = i
  return s
