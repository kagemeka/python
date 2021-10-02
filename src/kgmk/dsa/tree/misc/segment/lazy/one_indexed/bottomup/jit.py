from kgmk.dsa.math.bit_length.naive.jit import (
  bit_length,
)

# TODO cut below 

import typing 
import numpy as np 
import numba as nb 


S = typing.TypeVar('S')
F = typing.TypeVar('F')

@nb.njit 
def seg_build(
  op_s: typing.Callable[[S, S], S],
  e_s: typing.Callable[[], S],
  e_f: typing.Callable[[], F],
  a: np.ndarray,
) -> typing.Tuple[np.ndarray, np.ndarray]:
  n = 1 << bit_length(len(a) - 1)
  seg = np.empty((n << 1, ) + a.shape[1:], np.int64)
  for i in range(n << 1): seg[i] = e_s()
  seg[n:n + len(a)] = a.copy()
  for i in range(n - 1, 0, -1):
    seg[i] = op_s(seg[i << 1], seg[i << 1 | 1])
  lazy = np.empty(n, np.int64)
  for i in range(n): lazy[i] = e_f()
  return seg, lazy


@nb.njit 
def _seg_apply(
  seg: np.ndarray,
  lazy: np.ndarray,
  op_f: typing.Callable[[F, F], F],
  map: typing.Callable[[F, S], S],
  i: int,
  f: F,
) -> typing.NoReturn:
  seg[i] = map(f, seg[i])
  if i < len(lazy): lazy[i] = op_f(f, lazy[i])

  
@nb.njit
def _seg_propagate(
  seg: np.ndarray,
  lazy: np.ndarray,
  op_f: typing.Callable[[F, F], F],
  e_f: typing.Callable[[], F],
  map_: typing.Callable[[F, S], S],
  i: int,
) -> typing.NoReturn:
  _seg_apply(seg, lazy, op_f, map_, i << 1, lazy[i])
  _seg_apply(seg, lazy, op_f, map_, i << 1 | 1, lazy[i])
  lazy[i] = e_f()


@nb.njit 
def _seg_merge(
  seg: np.ndarray,
  op_s: typing.Callable[[S, S], S],
  i: int,
) -> typing.NoReturn:
  seg[i] = op_s(seg[i << 1], seg[i << 1 | 1])


@nb.njit 
def seg_set(
  seg: np.ndarray,
  lazy: np.ndarray,
  op_s: typing.Callable[[S, S], S],
  op_f: typing.Callable[[F, F], F],
  e_f: typing.Callable[[], F],
  map_: typing.Callable[[F, S], S],
  l: int,
  r: int,
  f: F,
) -> typing.NoReturn:
  n = len(seg) >> 1
  assert 0 <= l <= r <= n
  l, r = l + n, r + n
  h = bit_length(n)

  for i in range(h, 0, -1):
    if (l >> i) << i != l: 
      _seg_propagate(seg, lazy, op_f, e_f, map_, l >> i)  
    if (r >> i) << i != r:
      _seg_propagate(seg, lazy, op_f, e_f, map_, (r - 1) >> i)

  l0, r0 = l, r 
  while l < r:
    if l & 1:
      _seg_apply(seg, lazy, op_f, map_, l, f)
      l += 1
    if r & 1:
      r -= 1
      _seg_apply(seg, lazy, op_f, map_, r, f)
    l, r = l >> 1, r >> 1
  l, r = l0, r0
  for i in range(1, h + 1):
    if (l >> i) << i != l: _seg_merge(seg, op_s, l >> i)
    if (r >> i) << i != r: _seg_merge(seg, op_s, (r - 1) >> i)
    
  
@nb.njit 
def seg_get(
  seg: np.ndarray,
  lazy: np.ndarray,
  op_s: typing.Callable[[S, S], S],
  e_s: typing.Callable[[], S],
  op_f: typing.Callable[[F, F], F],
  e_f: typing.Callable[[], F],
  map_: typing.Callable[[F, S], S],
  l: int,
  r: int,
) -> S:
  n = len(seg) >> 1
  assert 0 <= l <= r <= n
  l, r = l + n, r + n
  h = bit_length(n)

  for i in range(h, 0, -1):
    if (l >> i) << i != l: 
      _seg_propagate(seg, lazy, op_f, e_f, map_, l >> i)  
    if (r >> i) << i != r:
      _seg_propagate(seg, lazy, op_f, e_f, map_, (r - 1) >> i)

  vl, vr = e_s(), e_s()
  while l < r:
    if l & 1:
      vl = op_s(vl, seg[l])
      l += 1
    if r & 1:
      r -= 1
      vr = op_s(seg[r], vr)
    l, r = l >> 1, r >> 1
  return op_s(vl, vr)


@nb.njit 
def seg_update(
  seg: np.ndarray,
  lazy: np.ndarray,
  op_s: typing.Callable[[S, S], S],
  op_f: typing.Callable[[F, F], F],
  e_f: typing.Callable[[], F],
  map_: typing.Callable[[F, S], S],
  i: int,
  x: S,
) -> typing.NoReturn:
  n = len(seg) >> 1
  assert 0 <= i <= n
  i += n
  h = bit_length(n)
  for j in range(h, 0, -1): 
    _seg_propagate(seg, lazy, op_f, e_f, map_, i >> j)
  seg[i] = x
  for j in range(1, h + 1): _seg_merge(seg, op_s, i >> j)