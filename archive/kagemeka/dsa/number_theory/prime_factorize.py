from .prime_numbers import (
  PrimeNumbers,
)


# cut below


from typing import (
  DefaultDict, 
)


from collections import (
  defaultdict,
)



class PrimeFactorize:
  

  def __init__(
    self,
    n: int= 1 << 20,
  ):
    self.pn = PrimeNumbers(n)
  

  def __call__(
    self,
    n: int,
  ) -> DefaultDict[int, int]:
    factors = defaultdict(int)
    for p in self.pn:
      if n < 2: 
        return factors
      if p * p > n: break
      while n % p == 0:
        factors[p] += 1
        n //= p
    factors[n] = 1
    return factors

    
  def factorial(
    self, 
    n: int,
  ) -> DefaultDict[int, int]:
    factors = defaultdict(int)
    for i in range(n + 1):
      for p, c in (
        self(i).items()
      ):
        factors[p] += c
    return factors