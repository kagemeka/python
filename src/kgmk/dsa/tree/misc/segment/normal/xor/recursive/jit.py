from kgmk.dsa.math.bit_length.jit import (
  bit_length,
)


# TODO cut below
import typing 
import numpy as np 
import numba as nb 



@nb.njit 
def seg_build(a: np.ndarray) -> np.ndarray:
  n = 1 << bit_length(len(a) - 1)
  seg = np.empty(n << 1, np.int64)
  seg[n:n + len(a)] = a 
  for i in range(n - 1, 0, -1):
    seg[i] = seg[i << 1] ^ seg[i << 1 | 1]
  return seg 


@nb.njit 
def seg_set(
  seg: np.ndarray, 
  i: int, 
  x: int,
) -> typing.NoReturn:
  i += len(seg) >> 1 
  seg[i] = x
  while i > 1:
    i >>= 1
    seg[i] = seg[i << 1] ^ seg[i << 1 | 1]


@nb.njit 
def seg_get(seg: np.ndarray, l: int, r: int) -> int:
  return _seg_get(seg, l, r, 0, len(seg) >> 1, 1)


@nb.njit 
def _seg_get(
  seg: np.ndarray, 
  l: int,
  r: int,
  s: int,
  t: int, 
  i: int,
) -> int:
  if t <= l or r <= s: return 0
  if l <= s and t <= r:
    return seg[i]
  c = (s + t) // 2 
  vl = _seg_get(seg, l, r, s, c, i << 1)
  vr = _seg_get(seg, l, r, c, t, i << 1 | 1)
  return vl ^ vr 