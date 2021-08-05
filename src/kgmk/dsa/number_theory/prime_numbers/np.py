from \
  ..sieve_of_eratosthenes.np \
import (
  SieveOfEratosthenes,
)
# TODO cut below


import numpy as np
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
    a = np.flatnonzero(fn(n))
    self.__a = a


  def __iter__(
    self,
  ) -> typing.Iterator[int]:
    return iter(self.__a)


  def __repr__(self) -> str:
    return f'{self.__a}'