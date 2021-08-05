from ..sieve_of_eratosthenes \
import (
  SieveOfEratosthenes,
)
# TODO cut below

import typing



class PrimeNumbers():
  def __getitem__(
    self,
    i: int,
  ) -> int:
    return self.__a[i] 


  def __init__(
    self, 
    n: int = 1 << 20,
  ) -> typing.NoReturn:
    fn = SieveOfEratosthenes()
    a = fn(n)
    self.__a = tuple(
      i for i in range(n) 
      if a[i]
    )


  def __iter__(
    self,
  ) -> typing.Iterator[int]:
    return iter(self.__a)


  def __repr__(self) -> str:
    return f'{self.__a}'