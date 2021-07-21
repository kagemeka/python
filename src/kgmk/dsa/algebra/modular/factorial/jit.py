import numpy as np
import numba as nb



@nb.njit
def cumprod(
  a: np.array,
  modulo: int,
) -> np.array:
  n = a.shape[0]
  for i in range(n - 1):
    a[i + 1] *= a[i]
    a[i + 1] %= modulo
  

@nb.njit
def factorial(
  n: int,
  modulo: int,
) -> np.array:
  a = np.arange(n); a[0] = 1
  cumprod(a, modulo)
  return a


@nb.njit
def mpow(
  x: int,
  n: int,
  modulo: int,
) -> int:
  if n == 0: return 1
  m = modulo
  y = mpow(x, n >> 1, m)
  y = y * y % m
  if n & 1: y = y * x % m
  return y


@nb.njit
def inv_factorial(
  n: int,
  modulo: int,
) -> np.array:
  m = modulo 
  x = factorial(n, m)[-1]
  a = np.arange(1, n + 1)
  a[-1] = mpow(x, m - 2, m)
  cumprod(a[::-1], m)
  return a