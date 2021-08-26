import numpy as np
import numba as nb


@nb.njit
def mod_matrix_dot(
  a: np.ndarray,
  b: np.ndarray,
  mod: int,
) -> np.ndarray:
  r, c = a.shape
  h, w = b.shape
  assert c == h
  c = np.zeros(
    (r, w), 
    dtype=np.int64,
  )
  for i in range(r):
    for j in range(w):
      c[i, j] = np.sum(a[i] * b[:, j] % mod) % mod 
  return c