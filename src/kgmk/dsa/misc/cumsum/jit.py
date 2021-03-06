import typing 
import numpy as np 
import numba as nb


@nb.njit
def cumsum(a: np.ndarray) -> typing.NoReturn:
  for i in range(len(a) - 1): a[i + 1] += a[i]