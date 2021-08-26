from ..dot.with_decomposition.np import (
  ModMatrixDot,
)


# TODO cut below

import numpy as np
import typing



class ModMatrixPow():
  def __call__(
    self,
    a: np.ndarray,
    n: int,
  ) -> np.ndarray:
    if n == 0:
      return np.identity(
        a.shape[0],
        dtype=np.int64,
      )
    x = self(a, n >> 1)
    x = self.__dot(x, x)
    if n & 1:
      x = self.__dot(x, a)
    return x


  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__dot = ModMatrixDot(mod)

