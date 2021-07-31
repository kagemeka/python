from ..factorial.np import (
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
    a = fn.inv(n)
    a[1:] *= fn(n - 1)
    self.__a = a % m 

  
  def __repr__(self) -> str:
    return str(self.__a)