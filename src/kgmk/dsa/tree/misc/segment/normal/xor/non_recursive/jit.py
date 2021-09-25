import typing 
import numpy as np 
import numba as nb 


@nb.njit 
def seg_build(a: np.ndarray) -> np.ndarray:
  n = len(a)
  seg = np.empty(n << 1, np.int64)
  seg[n:] = a 
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
  n = len(seg) >> 1
  l, r = l + n, r + n 
  v = 0
  while l < r:
    if l & 1:
      v ^= seg[l]
      l += 1
    if r & 1:
      r -= 1
      v ^= seg[r]
    l, r = l >> 1, r >> 1
  return v