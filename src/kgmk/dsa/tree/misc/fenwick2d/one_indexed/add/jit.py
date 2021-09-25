import typing 
import numpy as np 
import numba as nb 


@nb.njit
def fw_build(a: np.ndarray) -> np.ndarray:
  n, m = a.shape[:2]
  fw = np.empty((n + 1, m + 1) + a.shape[2:], np.int64)
  fw[1:, 1:] = a.copy()
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      k = j + (j & -j)
      if k < m + 1: fw[i, k] += fw[i, j]
  for j in range(1, m + 1):
    for i in range(1, n + 1):
      k = i + (i & -i)
      if k < n + 1: fw[k, j] += fw[i, j]
  return fw


@nb.njit
def fw_set(
  fw: np.ndarray, 
  i: int, 
  j: int, 
  x: int,
) -> typing.NoReturn:
  n, m = fw.shape
  j0 = j
  while i < n:
    j = j0
    while j < m:
      fw[i, j] += x
      j += j & -j
    i += i & -i


@nb.njit
def fw_get(fw: np.ndarray, i: int, j:int) -> int:
  v = 0
  i, j = i + 1, j + 1
  j0 = j 
  while i > 0:
    j = j0
    while j > 0:
      v += fw[i, j]
      j -= j & -j
    i -= i & -i
  return v 
