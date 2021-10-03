from kgmk.dsa.algebra.modular.factorial.np import (
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
    a = fn.inv(n)
    a[1:] *= fn(n - 1)
    self.__a = a % mod

  