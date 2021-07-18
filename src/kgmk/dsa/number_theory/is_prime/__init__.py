from ..sieve_of_eratosthenes \
import (
  SieveOfEratosthenes,
)
# TODO cut below


import typing



class IsPrime():
  def __call__(
    self,
    i: int,
  ) -> bool:
    return self.__a[i]


  def __getitem__(
    self,
    i: int,
  ) -> bool:
    return self(i) 


  def __init__(
    self,
    n: int = 1 << 20,
  ) -> typing.NoReturn:
    fn = SieveOfEratosthenes()
    self.__a = fn(n)


  def __repr__(
    self,
  ) -> str:
    return f'{self.__a}'