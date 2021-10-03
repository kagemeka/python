from kgmk.dsa.algebra.modular.factorial import (
  ModFactorial,
)

# TODO cut below


import typing


class ModInverseTable():
  def __call__(self, i: int) -> int: return self[i]
  def __getitem__(self, i: int) -> int: return self.__a[i]
  def __repr__(self) -> str: return str(self.__a)


  def __init__(self, n: int, mod: int) -> typing.NoReturn:
    fn = ModFactorial(mod)
    b = fn(n)
    a = fn.inv(n)
    for i in range(n - 1): a[i + 1] = (a[i + 1] * b[i]) % mod
    self.__a = a
