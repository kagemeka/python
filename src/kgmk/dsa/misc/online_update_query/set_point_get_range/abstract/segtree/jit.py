from \
  kgmk.dsa.tree.misc.segment.normal.one_indexed \
  .bottomup.jit \
import (
  seg_build,
  seg_set,
  seg_get,
)
  


# TODO cut below 

import typing 
import numpy as np 
import numba as nb 



S = typing.TypeVar('S')
@nb.njit 
def seg_op(a: S, b: S) -> S:
  return ...


@nb.njit 
def seg_e() -> S:
  return ...


@nb.njit 
def build_seg(a: np.ndarray) -> np.ndarray:
  return seg_build(seg_op, seg_e, a)
  

@nb.njit 
def set_point_seg(
  seg: np.ndarray, 
  i: int, 
  x: S,
) -> typing.NoReturn:
  seg_set(seg, seg_op, i, x)


@nb.njit 
def get_range_seg(seg: np.ndarray, l: int, r: int) -> S:
  return seg_get(seg, seg_op, seg_e, l, r)