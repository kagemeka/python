from ...abstract.fenwick.jit import (
  build_fw,
  set_point_fw,
  get_half_range_fw,
)

# TODO cut below 
import numba as nb 



@nb.njit
def fw_op(a: int, b: int) -> int:
  return max(a, b)


@nb.njit 
def fw_e() -> int:
  return -(1 << 60)

