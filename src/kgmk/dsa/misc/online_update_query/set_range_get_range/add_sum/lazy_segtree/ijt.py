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
  return a + b


@nb.njit 
def seg_e_s() -> S:
  return np.zeros(2, np.int64)


@nb.njit 
def seg_op_f(f: F, g: F) -> F:
  return f + g


@nb.njit 
def seg_e_f() -> F:
  return 0 


@nb.njit 
def seg_map(f: F, x: S) -> S:
  x = x.copy()
  x[0] += f * x[1]
  return x
