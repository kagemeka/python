from kgmk.dsa.tree.misc.fenwick.one_indexed.jit import (
  fw_build,
  fw_get,
  fw_set,
)


# TODO cut below 

import typing 
import numpy as np 
import numba as nb 


S = typing.TypeVar('S')
@nb.njit
def fw_op(a: S, b: S) -> S:
  return ... 


@nb.njit 
def fw_e() -> S:
  return ...


@nb.njit 
def build_fw(a: np.ndarray) -> np.ndarray:
  return fw_build(fw_op, a)


@nb.njit 
def set_point_fw(
  fw: np.ndarray, 
  i: int, 
  x: int,
) -> typing.NoReturn:
  fw_set(fw, fw_op, i, x)


@nb.njit 
def get_range_fw(fw: np.ndarray, l: int, r: int) -> int:
  return fw_op(
    fw_get(fw, fw_op, fw_e, r - 1), 
    fw_get(fw, fw_op, fw_e, l - 1),
  )
