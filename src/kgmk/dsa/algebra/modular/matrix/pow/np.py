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
    x = np.identity(
      a.shape[0],
      dtype=np.int64,
    )
    while n:
      if n & 1: x = self.__dot(x, a)
      a = self.__dot(a, a)
      n >>= 1
    return x
      

  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__dot = ModMatrixDot(mod)