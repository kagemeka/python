import typing 
import sys 
import numpy as np 
import numba as nb 

from kgmk.dsa.tree.misc.segment.lazy.bottomup.jit import (
  seg_build,
  seg_get,
  seg_set,
  seg_update,
  S,
  F,
)

# TODO cut below


@nb.njit 
def seg_op_s(a: S, b: S) -> S:
  return ...


@nb.njit 
def seg_e_s() -> S:
  return ...


@nb.njit 
def seg_op_f(f: F, g: F) -> F:
  return ...


@nb.njit 
def seg_e_f() -> F:
  return ...


@nb.njit 
def seg_map(f: F, x: S) -> S:
  return ...


@nb.njit 
def build_seg(
  a: np.ndarray,
) -> typing.Tuple[np.ndarray, np.ndarray]:
  return seg_build(seg_op_s, seg_e_s, seg_e_f, a)


@nb.njit 
def set_range_seg(
  seg: np.ndarray, 
  lazy: np.ndarray,
  l: int,
  r: int,
  f: F,
) -> typing.NoReturn:
  seg_set(
    seg, lazy, 
    seg_op_s, seg_op_f, seg_e_f, seg_map,
    l, r, f,
  )


@nb.njit 
def get_range_seg(
  seg: np.ndarray,
  lazy: np.ndarray,
  l: int,
  r: int,
) -> S:
  return seg_get(
    seg, lazy,
    seg_op_s, seg_e_s, seg_op_f, seg_e_f, seg_map,
    l, r,
  )


@nb.njit 
def update_point_seg(
  seg: np.ndarray,
  lazy: np.ndarray,
  i: int,
  x: S,
) -> typing.NoReturn:
  seg_update(
    seg, lazy, 
    seg_op_s, seg_op_f, seg_e_f, seg_map,
    i, x
  )