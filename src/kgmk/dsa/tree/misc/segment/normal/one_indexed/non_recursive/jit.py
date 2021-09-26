import typing 
import numpy as np 
import numba as nb 


S = typing.TypeVar('S')

@nb.njit 
def seg_build(
  op: typing.Callable[[S, S], S],
  a: np.ndarray,
) -> np.ndarray:
  n = len(a)
  seg = np.empty((n << 1, ) + a.shape[1:], np.int64)
  seg[n:] = a.copy()
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