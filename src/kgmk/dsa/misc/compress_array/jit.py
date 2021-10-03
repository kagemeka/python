import typing 
import numpy as np 
import numba as nb 



@nb.njit 
def compress_array(
  a: np.ndarray,
) -> typing.Tuple[(np.ndarray, ) * 2]:
  v = np.unique(a)
  i = np.searchsorted(v, a)
  return i, v
