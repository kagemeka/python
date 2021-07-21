import numpy as np
import numba as nb



@nb.njit
def mdot(
  a: np.array,
  b: np.array,
  modulo: int,
) -> np.array:
  r, c = a.shape
  h, w = b.shape
  assert c == h
  c = np.zeros(
    (r, w), 
    dtype=np.int64,
  )
  m = modulo
  for i in range(r):
    for j in range(w):
      c[i, j] = np.sum(
        a[i] * b[:, j] % m,
      ) % m 
  return c 
      

@nb.njit
def matpow(
  a: np.ndarray,
  n: int,
  modulo: int,
) -> np.ndarray:
  if n == 0:
    return np.eye(
      a.shape[0],
      dtype=np.int64,
    ) 
  m = modulo 
  x = matpow(a, n >> 1, m)
  x = mdot(x, x, m)
  if n & 1: 
    x = mdot(x, a, m)
  return x