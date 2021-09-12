import typing 
import numpy as np 
import numba as nb 


@nb.njit((nb.i8[:], ), cache=True)
def compress_array(
  a: np.ndarray,
) -> typing.Tuple[
  np.ndarray,
  np.ndarray,
]:
  v = np.unique(a)
  i = np.searchsorted(v, a)
  return i, v 
