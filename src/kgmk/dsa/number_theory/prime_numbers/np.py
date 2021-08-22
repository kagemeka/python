from ..sieve_of_eratosthenes.np import (
  SieveOfEratosthenes,
)
# TODO cut below


import numpy as np
import typing



class PrimeNumbers():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> np.array:
    s = SieveOfEratosthenes()(n)
    return np.flatnonzero(s)