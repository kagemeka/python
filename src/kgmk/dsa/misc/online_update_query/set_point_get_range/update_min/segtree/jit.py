from ...abstract.segtree.jit import (
  build_seg,
  set_point_seg,
  get_range_seg,
)

# TODO cut below 
import typing
import numba as nb 


S = typing.TypeVar('S')
@nb.njit 
def seg_op(a: S, b: S) -> S:
  return min(a, b)


@nb.njit 
def seg_e() -> S:
  return 1 << 60