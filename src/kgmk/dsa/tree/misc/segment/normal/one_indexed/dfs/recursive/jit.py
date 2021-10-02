from kgmk.dsa.math.bit_length.naive.jit import (
  bit_length,
)


# TODO cut below 
import typing 
import numpy as np 
import numba as nb 


S = typing.TypeVar('S')

@nb.njit 
def seg_build(
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  a: np.ndarray,
) -> np.ndarray:
  n = 1 << bit_length(len(a) - 1)
  seg = np.empty((n << 1, ) + a.shape[1:], np.int64)
  for i in range(n << 1): seg[i] = e()
  seg[n:n + len(a)] = a.copy()
  for i in range(n - 1, 0, -1):
    seg[i] = op(seg[i << 1], seg[i << 1 | 1])
  return seg 


@nb.njit 
def seg_set(
  seg: np.ndarray,
  op: typing.Callable[[S, S], S],
  i: int, 
  x: S,
) -> typing.NoReturn:
  i += len(seg) >> 1 
  seg[i] = x
  while i > 1:
    i >>= 1
    seg[i] = op(seg[i << 1], seg[i << 1 | 1])


@nb.njit 
def seg_get(
  seg: np.ndarray,
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  l: int, 
  r: int,
) -> int:
  return _seg_get(seg, op, e, l, r, 0, len(seg) >> 1, 1)


@nb.njit 
def _seg_get(
  seg: np.ndarray, 
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  l: int,
  r: int,
  s: int,
  t: int, 
  i: int,
) -> int:
  if t <= l or r <= s: return e()
  if l <= s and t <= r:
    return seg[i]
  c = (s + t) // 2 
  vl = _seg_get(seg, op, e, l, r, s, c, i << 1)
  vr = _seg_get(seg, op, e, l, r, c, t, i << 1 | 1)
  return op(vl, vr) 


@nb.njit 
def seg_get_point(seg: np.ndarray, i: int) -> int:
  return seg[i + (len(seg) >> 1)]