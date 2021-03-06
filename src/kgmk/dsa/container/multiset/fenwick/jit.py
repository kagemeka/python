# use with coordinates compression.
# values range is limited [0, n) because of Fenwick Tree.

from \
  kgmk.dsa.misc.online_update_query.set_point_get_range \
  .abstract.fenwick.jit \
import (
  build_fw,
  set_fw,
  get_fw,
  get_range_fw,
  max_right_fw,
)

from \
  kgmk.dsa.misc.online_update_query.set_point_get_range \
  .add_sum.fenwick.jit \
import (
  fw_op,
  fw_e,
  fw_inverse,
)


# TODO cut below
import typing
import numpy as np 
import numba as nb

@nb.njit 
def ms_build(n: int) -> np.ndarray:
  return build_fw(np.zeros(n, np.int64))

@nb.njit 
def ms_size(ms: np.ndarray) -> int:
  return get_fw(ms, len(ms) - 1)

@nb.njit 
def ms_add(ms: np.ndarray, x: int) -> typing.NoReturn:
  set_fw(ms, x, 1)

@nb.njit 
def ms_pop(ms: np.ndarray, x: int) -> typing.NoReturn:
  assert get_range_fw(ms, x, x + 1) > 0
  set_fw(ms, x, -1)

@nb.njit
def ms_get(ms: np.ndarray, i: int) -> int:
  assert 0 <= i < get_fw(ms, len(ms) - 1)
  is_ok = lambda v, x: v < x
  return max_right_fw(ms, is_ok, i + 1)

@nb.njit 
def ms_max(ms: np.ndarray) -> int: 
  return ms_get(ms, ms_size(ms) - 1)

@nb.njit 
def ms_min(ms: np.ndarray) -> int: return ms_get(ms, 0)

@nb.njit 
def ms_lower_bound(ms: np.ndarray, x: int) -> int:
  return get_fw(ms, x)

@nb.njit 
def ms_upper_bound(ms: np.ndarray, x: int) -> int:
  return get_fw(ms, x + 1)