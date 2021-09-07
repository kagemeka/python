import numpy as np
import numba as nb


@nb.njit
def mod_matrix_dot(
  a: np.ndarray,
  b: np.ndarray,
  mod: int,
) -> np.ndarray:
  ha, wa = a.shape
  hb, wb = b.shape
  assert wa == hb
  c = np.zeros((ha, wb), np.int64)
  for i in range(ha):
    for j in range(wb):
      c[i, j] = np.sum(a[i] * b[:, j] % mod) % mod 
  return c