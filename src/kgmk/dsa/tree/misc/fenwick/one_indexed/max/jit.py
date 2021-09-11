import typing 
import numpy as np 
import numba as nb 



@nb.njit(
  (nb.i8, ),
  cache=True,
)
def fw_build(
  n: int,
) -> np.ndarray:
  inf = 1 << 60
  return np.full(n + 1, -inf, np.int64)


@nb.njit(
  (nb.i8[:], ),
  cache=True,
)
def fw_build_from_array(
  a: np.ndarray,
) -> np.ndarray:
  inf = 1 << 60
  assert a[0] == -inf
  fw = a.copy()
  n = a.size 
  for i in range(n):
    j = i + (i & -i)
    if j < n: fw[j] = max(fw[j], fw[i])
  return fw


@nb.njit(
  (nb.i8[:], nb.i8, nb.i8),
  cache=True,
)
def fw_set(
  fw: np.ndarray,
  i: int,
  x: int,
) -> typing.NoReturn:
  while i < fw.size:
    fw[i] = max(fw[i], x)
    i += i & -i


@nb.njit(
  (nb.i8[:], nb.i8),
  cache=True,
)
def fw_get(
  fw: np.ndarray,
  i: int,
) -> int:
  v = -(1 << 60)
  while i > 0:
    v = max(v, fw[i])
    i -= i & -i
  return v 


@nb.njit(
  (nb.i8[:], nb.i8),
  cache=True,
)
def fw_lower_bound(
  fw: np.ndarray,
  x: int
) -> int:
  n = fw.size
  l = 1
  while l << 1 < n: l <<= 1
  v = -(1 << 60)
  i = 0 
  while l:
    if i + l < n and max(v, fw[i + l]) < x:
      i += l
      v = max(v, fw[i])
    l >>= 1
  return i + 1