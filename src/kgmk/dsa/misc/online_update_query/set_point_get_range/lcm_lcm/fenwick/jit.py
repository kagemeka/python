from ...abstract.fenwick.jit import (
  build_fw,
  set_point_fw,
  get_range_fw,
)
from kgmk.dsa.math.lcm.jit import (
  lcm,
)

# TODO cut below 
import numba as nb 



@nb.njit
def fw_op(a: int, b: int) -> int:
  return lcm(a, b)


@nb.njit 
def fw_e() -> int:
  return 1

