from ..cumprod.np import (
  ModCumprod,
)

# TODO cut below 


import typing
import numpy as np




class ModFactorial():
  def __call__(
    self,
    n: int=1 << 20,
  ) -> np.array:
    cumprod = ModCumprod(self.__mod)
    a = np.arange(n)
    a[0] = 1
    return cumprod(a)
  

  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__mod = mod


  def inv(
    self,
    n: int=1 << 20,
  ) -> np.array:
    mod = self.__mod
    a = np.arange(1, n + 1)
    a[-1] = pow(int(self(n)[-1]), mod - 2, mod)
    return ModCumprod(mod)(a[::-1])[::-1]
