from ..factorial import (
  ModFactorial,
)


# TODO cut below


import typing



class Inverse():
  def __call__(
    self,
    i: int,
  ) -> int:
    return self[i]


  def __getitem__(
    self,
    i: int,
  ) -> int:
    return self.__a[i]


  def __init__(
    self,
    n: int,
    modulo: int,
  ) -> typing.NoReturn:
    m = modulo
    fn = ModFactorial(m)
    b = fn(n)
    a = fn.inv(n)
    for i in range(n - 1):
      a[i + 1] *= b[i]
      a[i + 1] %= m
    self.__a = a