from ...algebra.modular.factorial.np import (
  ModFactorial,
)


# TODO cut below


import typing




class ModChoose():
  def __call__(
    self,
    n: int,
    k: int,
  ) -> int:
    ok = (0 <= k) & (k <= n)
    m = self.__mod
    f, i = self.__fact, self.__ifact
    c = f[n] * i[k] % m * i[n - k] % m
    return c * ok
  

  def __init__(
    self,
    mod: int,
    n: int = 1 << 20,
  ) -> typing.NoReturn:
    self.__mod = mod
    factorial = ModFactorial(mod)
    self.__fact = factorial(n)
    self.__ifact = factorial.inv(n)


  def inv(
    self,
    n: int,
    k: int,
  ) -> int:
    ok = (0 <= k) & (k <= n)
    m = self.__mod
    f, i = self.__fact, self.__ifact
    c = i[n] * f[k] % m * f[n - k] % m
    return c * ok
  