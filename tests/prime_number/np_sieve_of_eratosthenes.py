from \
  kgmk.dsa.number_theory \
  .sieve_of_eratosthenes.np \
import (
  SieveOfEratosthenes,
)
import numpy as np



def test():
  fn = SieveOfEratosthenes()
  a = fn(100)
  print(a)
  print(np.flatnonzero(a))
  a = fn.spf(100)
  print(a)



if __name__ == '__main__':
  test()