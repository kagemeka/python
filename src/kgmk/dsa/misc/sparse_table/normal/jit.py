from kgmk.dsa.math.bit_length.table.jit import (
  bit_length_table,
)

# TODO cut below 
import typing 
import numpy as np 
import numba as nb 



S = typing.TypeVar('S')
@nb.njit 
def sparse_table_build(
  bit_len: np.ndarray,
  op: typing.Callable[[S, S], S],
  a: np.ndarray,
) -> np.ndarray:
  n = len(a)
  k = bit_len[n]
  table = np.empty((k, ) + a.shape, np.int64)
  table[0] = a.copy()
  for i in range(k - 1):
    table[i + 1] = table[i].copy()
    for j in range(n - (1 << i)):
      table[i + 1, j] = op(table[i, j], table[i, j + (1 << i)])
  return table


@nb.njit 
def sparse_table_get(
  bit_len: np.ndarray,
  table: np.ndarray, 
  op: typing.Callable[[S, S], S],
  l: int, 
  r: int,
) -> S:
  k = bit_len[r - l] - 1
  return op(table[k, l], table[k, r - (1 << k)])



@nb.njit 
def sparse_table_op(x: S, y: S) -> S:
  return ...
  