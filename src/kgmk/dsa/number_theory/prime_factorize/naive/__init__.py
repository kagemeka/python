import typing 
import collections



class PrimeFactorize():
  def __call__(
    self,
    n: int,
  ) -> typing.DefaultDict[int, int]:
    f = collections.defaultdict(int)
    i = 2
    while i * i <= n:
      while n % i == 0:
        n //= i
        f[i] += 1
      i += 1
    if n > 1: f[n] = 1
    return f
  

  def factorial(
    self,
    n: int,
  ) -> typing.DefaultDict[int, int]:
    f = collections.defaultdict(int)
    for i in range(n + 1):
      for p, c in self(i).items(): 
        f[p] += c
    return f