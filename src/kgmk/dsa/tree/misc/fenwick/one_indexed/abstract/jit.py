import typing 
import numpy as np 
import numba as nb 


@nb.njit
def fw_build(
  n: int,
  e: int,
) -> np.ndarray:
  return np.full(n + 1, e, np.int64)


@nb.njit
def fw_build_from_array(
  a: np.ndarray,
  fn: typing.Callable[[int, int], int],
  e: int,
) -> np.ndarray:
  assert a[0] == e
  fw = a.copy()
  n = fw.size  
  for i in range(n):
    j = i + (i & -i)
    if j < n: 
      fw[j] = fn(fw[j], fw[i])
  return fw 


@nb.njit
def fw_set(
  fw: np.ndarray,
  i: int,
  x: int,
  fn: typing.Callable[[int, int], int],
) -> typing.NoReturn:
  while i < len(fw):
    fw[i] = fn(fw[i], x)
    i += i & -i


@nb.njit
def fw_get(
  fw: np.ndarray,
  i: int,
  fn: typing.Callable[[int, int], int],
  e: int,
) -> int:
  v = e 
  while i > 0:
    v = fn(v, fw[i])
    i -= i & -i
  return v 
  

# if abbelian group
@nb.njit 
def fw_get_range(
  fw: np.ndarray,
  l: int,
  r: int,
  fn: typing.Callable[[int, int], int],
  e: int,
  inverse: typing.Callable[[int], int],
) -> int:
  lv = fw_get(fw, l - 1, fn, e)
  rv = fw_get(fw, r, fn, e)
  return fn(inverse(lv), rv)


# if monotonic increasing 
@nb.njit
def fw_lower_bound(
  fw: np.ndarray,
  fn: typing.Callable[[int, int], int],
  e: int,
  search_fn: typing.Callable[[int], bool],
  k: int, # it's impossible to use closure with numba(v0.53.1).
) -> int:
  n = fw.size
  l = 1
  while l << 1 < n: l <<= 1
  v = e
  i = 0 
  while l:
    if i + l < n and not search_fn(fn(v, fw[i + l]), k):
      i += l
      v = fn(v, fw[i])
    l >>= 1
  return i + 1
  