from \
  ...algebra.modular \
  .factorial \
import (
  ModFactorial,
)


# TODO cut below


import typing



class Choose():
  def __call__(
    self,
    n: int,
    r: int,
  ) -> int:
    a, b = self.__a, self.__b
    m = self.__mod
    ok = 0 <= r <= n
    c = a[n] * b[n - r] % m
    return c * b[r] % m * ok
  

  def __init__(
    self,
    n: int,
    modulo: int,
  ) -> typing.NoReturn:
    fn = ModFactorial(modulo)
    self.__a = fn(n)
    self.__b = fn.inv(n)
    self.__mod = modulo