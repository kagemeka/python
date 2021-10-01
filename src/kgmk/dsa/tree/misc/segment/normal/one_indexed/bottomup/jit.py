from kgmk.dsa.math.bit_length.jit import (
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
  n = len(seg) >> 1
  l, r = l + n, r + n 
  vl = vr = e()
  while l < r:
    if l & 1:
      vl = op(vl, seg[l])
      l += 1
    if r & 1:
      r -= 1
      vr = op(seg[r], vr)
    l, r = l >> 1, r >> 1
  return op(vl, vr)


@nb.njit
def seg_max_right(
  seg: np.ndarray,
  op: np.ndarray,
  e: np.ndarray,
  is_ok: typing.Callable[[S], bool],
  x: S,
  l: int,
  size: int,
) -> int:
  n = len(seg) >> 1 
  assert 0 <= l < size
  i = l + n
  v = e()
  while True:
    i //= i & -i
    if is_ok(op(v, seg[i]), x):
      v = op(v, seg[i])
      i += 1
      if i & -i == i: return size
      continue
    while i < n:
      i <<= 1
      if not is_ok(op(v, seg[i]), x): continue
      v = op(v, seg[i])
      i += 1
    return i - n