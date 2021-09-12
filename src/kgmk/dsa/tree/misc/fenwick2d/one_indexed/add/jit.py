import typing 
import numpy as np 
import numba as nb 



@nb.njit((nb.i8, nb.i8), cache=True)
def fw_build(n: int, m: int) -> np.ndarray:
  return np.zeros((n + 1, m + 1), np.int64)


@nb.njit((nb.i8[:, :], ), cache=True)
def fw_build_from_array(a: np.ndarray) -> np.ndarray:
  n, m = a.shape
  assert np.all(a[0] == 0) and np.all(a[:, 0] == 0)
  fw = a.copy()
  for i in range(n):
    for j in range(m):
      k = j + (j & -j)
      if k < m: fw[i, k] += fw[i, j]
  for j in range(m):
    for i in range(n):
      k = i + (i & -i)
      if k < n: fw[k, j] += fw[i, j]
  return fw


@nb.njit((nb.i8[:, :], nb.i8, nb.i8, nb.i8), cache=True)
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


@nb.njit((nb.i8[:, :], nb.i8, nb.i8), cache=True)
def fw_get(fw: np.ndarray, i: int, j:int) -> int:
  v = 0
  j0 = j 
  while i > 0:
    j = j0
    while j > 0:
      v += fw[i, j]
      j -= j & -j
    i -= i & -i
  return v 
