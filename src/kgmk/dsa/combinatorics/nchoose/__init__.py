from \
  ...algebra.modular \
  .factorial \
import (
  ModFactorial,
)

# TODO cut below


import typing



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
    a = list(range(
      n + 1,
      n - r,
      -1,
    )); a[0] = 1
    fn.cumprod(a)
    b = fn.inv(r + 1)
    for i in range(rmax + 1):
      a[i] *= b[i]
      a[i] %= m
    self.__a = a
  

  def __len__(self) -> int:
    return len(self.__a)
