import typing 
import numpy as np 
import numba as nb 


S = typing.TypeVar('S')

@nb.njit 
def fw_build(
  op: typing.Callable[[S, S], S], 
  a: np.ndarray,
) -> np.ndarray:
  n = len(a)
  fw = np.empty((n + 1, ) + a.shape[1:], np.int64)
  fw[1:] = a.copy()
  for i in range(1, n + 1):
    j = i + (i & -i)
    if j < n + 1: fw[j] = op(fw[j], fw[i])
  return fw 


@nb.njit 
def fw_set(
  op: typing.Callable[[S, S], S],
  fw: np.ndarray,
  i: int,
  x: S,
) -> typing.NoReturn:
  assert 0 <= i < len(fw) - 1
  i += 1
  while i < len(fw):
    fw[i] = op(fw[i], x)
    i += i & -i 


@nb.njit 
def fw_get(
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  fw: np.ndarray,
  i: int,
) -> S:
  assert 0 <= i < len(fw)
  v = e()
  while i > 0:
    v = op(v, fw[i])
    i -= i & -i 
  return v 


@nb.njit
def fw_max_right(
  fw: np.ndarray,
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  is_ok: typing.Callable[[S], bool], # fn(v) -> bool
  x: S, # fn(v, x) cuz closure is not supported on v0.53.1.
) -> int:
  n = len(fw)
  l = 1
  while l << 1 < n: l <<= 1
  v, i = e(), 0
  while l:
    if i + l < n and is_ok(op(v, fw[i + l]), x):
      i += l
      v = op(v, fw[i])
    l >>= 1
  return i