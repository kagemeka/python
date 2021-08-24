from ..cumprod import (
  ModCumprod,
)

# TODO cut below
import typing



class ModFactorial():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    a = list(range(n))
    a[0] = 1
    ModCumprod(self.__mod)(a)
    return a


  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__mod = mod 
  

  def inv(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    a = list(range(1, n + 1))
    mod = self.__mod
    a[-1] = pow(self(n)[-1], mod - 2, mod)
    a.reverse()
    ModCumprod(mod)(a)
    return a[::-1]
