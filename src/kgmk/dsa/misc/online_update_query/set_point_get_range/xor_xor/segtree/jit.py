from ...abstract.segtree.jit import (
  build_seg,
  set_point_seg,
  get_range_seg,
)

# TODO cut below 
import numba as nb 


@nb.njit 
def seg_op(a: int, b: int) -> int:
  return ...


@nb.njit 
def seg_e() -> int:
  return 0