from \
  kgmk.dsa.number_theory \
  .sieve_of_eratosthenes \
import (
  SieveOfEratosthenes,
)



def test():
  fn = SieveOfEratosthenes()
  a = fn(100)
  print(a)
  a = fn.spf(100)
  print(a)



if __name__ == '__main__':
  test()