from ...prime_numbers import (
  PrimeNumbers,
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
    for p in self.__pn:
      if p * p > n: break
      while n % p == 0:
        n //= p 
        f[p] += 1
    if n > 1: f[n] = 1
    return f
  

  def __init__(
    self,
    max_n: int = 1 << 40,
  ) -> typing.NoReturn:
    n = 1
    while n * n <= max_n:
      n <<= 1
    self.__pn = PrimeNumbers()(n)
  

  def factorial(
    self,
    n: int,
  ) -> typing.List[int]:
    f = collections.defaultdict(int)
    for i in range(n + 1):
      for p, c in self(i).items():
        f[p] += c
    return f