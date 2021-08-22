from ...sieve_of_eratosthenes import (
  SieveOfEratosthenes,
)

# TODO cut below

import typing
import collections


class PrimeFactorize():
  def __call__(
    self,
    n: int,
  ) -> typing.DefaultDict[int, int]:
    f = collections.defaultdict(int)
    while n > 1:
      p = self.__lpf[n]
      n //= p 
      f[p] += 1
    return f
  

  def __init__(
    self,
    n: int = 1 << 20,
  ) -> typing.NoReturn:
    self.__lpf = SieveOfEratosthenes().lpf(n)
  

  def factorial(
    self,
    n: int,
  ) -> typing.List[int]:
    f = collections.defaultdict(int)
    for i in range(n + 1):
      for p, c in self(i).items():
        f[p] += c
    return f
