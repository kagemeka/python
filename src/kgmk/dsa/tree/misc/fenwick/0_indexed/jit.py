import typing 
import numpy as np 
import numba as nb 


@nb.njit
def fw_build(
  n: int,
  e: int,
) -> np.ndarray:
  fw = np.full(n + 1, e, np.int64)
  return fw


@nb.njit
def fw_get(
  fw: np.ndarray,
  i: int,
  fn: typing.Callable[[int, int], int],
  e: int,
) -> int:
  v = e
  while i > 0:
    v = fn(v, fw[i])
    i -= i & -i
  return v


@nb.njit
def fw_set(
  fw: np.ndarray,
  i: int,
  x: int,
  fn: typing.Callable[[int, int], int],
) -> typing.NoReturn:
  while i < len(fw):
    fw[i] = fn(fw[i], x)
    i += i & -i