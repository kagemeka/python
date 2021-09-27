from ...abstract.lazy_segtree.jit import (
  S,
  F,
  build_seg,
  set_range_seg,
  get_range_seg,
  update_point_seg,
)

# TODO cut below 

import numpy as np 
import numba as nb 


@nb.njit 
def seg_op_s(a: S, b: S) -> S:
  return max(a, b)


@nb.njit 
def seg_e_s() -> S:
  return -(1 << 60)


@nb.njit 
def seg_op_f(f: F, g: F) -> F:
  return g if f == seg_e_f() else f


@nb.njit 
def seg_e_f() -> F:
  return -1


@nb.njit 
def seg_map(f: F, x: S) -> S:
  return x if f == seg_e_f() else f