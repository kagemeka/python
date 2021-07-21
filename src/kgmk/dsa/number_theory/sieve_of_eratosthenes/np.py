import numpy as np 
import typing



class SieveOfEratosthenes():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> np.array:
    s = self.spf(n)
    return s == np.arange(n)
  

  def spf(
    self,
    n: int,
  ) -> np.array:
    s = np.arange(n)
    s[:2] = -1
    i = 0
    while i * i < n:
      i += 1
      if s[i] != i: continue
      s[i * 2::i] = i
    return s