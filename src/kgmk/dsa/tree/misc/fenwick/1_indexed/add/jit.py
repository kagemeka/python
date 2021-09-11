import typing 
import numpy as np
import numba as nb 



@nb.njit(
  (nb.i8, ),
  cache=True,
)
def fw_build(n: int) -> np.ndarray:
  return np.full(n + 1, 0, np.int64)


@nb.njit(
  (nb.i8[:], ),
  cache=True,
) 
def fw_build_from_array(
  a: np.ndarray,
) -> np.ndarray:
  assert a[0] == 0 
  fw = a.copy()
  n = fw.size
  for i in range(n):
    j = i + (i & -i)
    if j < n: fw[j] += fw[i]
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
  while i < len(fw):
    fw[i] += x
    i += i & -i


@nb.njit(
  (nb.i8[:], nb.i8),
  cache=True,
)
def fw_get(
  fw: np.ndarray,
  i: int,
) -> int:
  v = 0 
  while i > 0:
    v += fw[i]
    i -= i & -i
  return v 


@nb.njit(
  (nb.i8[:], nb.i8, nb.i8),
  cache=True,
)
def fw_get_range(
  fw: np.ndarray,
  l: int,
  r: int,
) -> int:
  return -fw_get(fw, l - 1) + fw_get(fw, r)



# if monotonic increasing.
# different per problem
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
  v = 0 
  i = 0 
  while l:
    if i + l < n and v + fw[i + l] < x:
      i += l
      v += fw[i]
    l >>= 1
  return i + 1