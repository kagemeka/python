from ..prime_numbers.np \
import (
  PrimeNumbers,
)
# TODO cut below


from typing import (
  DefaultDict, 
)
from collections import (
  defaultdict,
)


class PrimeFactorize:
  def __call__(
    self,
    n: int,
  ) -> DefaultDict[int, int]:
    f = defaultdict(int)
    for p in self.__pn:
      if n < 2: return f
      if p * p > n: break
      while n % p == 0:
        f[p] += 1
        n //= p
    f[n] = 1; return f
  

  def __init__(
    self,
    n: int = 1 << 20,
  ):
    pn = PrimeNumbers(n)
    self.__pn = tuple(pn)

    
  def factorial(
    self, 
    n: int,
  ) -> DefaultDict[int, int]:
    f = defaultdict(int)
    for i in range(n + 1):
      for (
        p, c,
      ) in self(i).items():
        f[p] += c
    return f