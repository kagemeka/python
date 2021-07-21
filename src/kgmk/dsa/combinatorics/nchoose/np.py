from \
  ...algebra.modular \
  .factorial.np \
import (
  ModFactorial,
)
  



import typing
import numpy as np


class NChoose():
  def __call__(
    self,
    r: int,
  ) -> int:
    return self[r]

  
  def __getitem__(
    self,
    r: int,
  ) -> int:
    return self.__a[r]
  

  def __init__(
    self,
    n: int,
    rmax: int,
    modulo: int,
  ) -> typing.NoReturn:
    r, m = rmax, modulo
    fn = ModFactorial(m)
    a = np.arange(
      n + 1,
      n - r,
      -1,
    ); a[0] = 1
    a = fn.cumprod(a)
    a *= fn.inv(r + 1)
    self.__a = a % m
  

  def __len__(self) -> int:
    return self.__a.size