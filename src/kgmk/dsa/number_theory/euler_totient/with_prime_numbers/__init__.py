from ...prime_numbers import (
  PrimeNumbers,
)

# TODO cut below

import typing


class EulerTotient():
  def __call__(
    self,
    n: int,
  ) -> int:
    c = n
    for p in self.__pn:
      if p * p > n: break
      if n % p: continue
      c = c // p * (p - 1)
      while not n % p: n //= p
    if n > 1:
      c = c // n * (n - 1)
    return c
    

  def __init__(
    self,
    n: int = 1 << 20,
  ) -> typing.NoReturn:
    self.__pn = PrimeNumbers(n)