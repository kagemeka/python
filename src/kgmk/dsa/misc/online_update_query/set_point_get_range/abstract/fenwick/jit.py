from kgmk.dsa.tree.misc.fenwick.one_indexed.jit import (
  fw_build,
  fw_get,
  fw_set,
)


# TODO cut below 

import typing 
import numpy as np 
import numba as nb 


@nb.njit 
def build_fw(a: np.ndarray) -> np.ndarray:
  return fw_build(fw_op, a)


S = typing.TypeVar('S')
@nb.njit 
def set_fw(fw: np.ndarray, i: int, x: S) -> typing.NoReturn:
  fw_set(fw_op, fw, i, x)


@nb.njit
def get_fw(fw: np.ndarray, i: int) -> S:
  return fw_get(fw_op, fw_e, fw, i)


@nb.njit 
def get_range_fw(fw: np.ndarray, l: int, r: int) -> S:
  return fw_op(
    fw_inverse(fw_get(fw_op, fw_e, fw, l)),
    fw_get(fw_op, fw_e, fw, r),
  )


@nb.njit 
def fw_inverse(a: S) -> S: return ...


@nb.njit 
def fw_op(a: S, b: S) -> S: return ...


@nb.njit 
def fw_e() -> S: return 0
