from ..sieve_of_eratosthenes import (
  SieveOfEratosthenes,
)
# TODO cut below

import typing


class PrimeNumbers():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    s = SieveOfEratosthenes()(n)
    return [i for i in range(n) if s[i]]