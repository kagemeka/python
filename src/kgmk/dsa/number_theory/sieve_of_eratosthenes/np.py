import numpy as np 



class SieveOfEratosthenes():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> np.array:
    s = self.gpf(n)
    return s == np.arange(n)
  

  def gpf(
    self,
    n: int = 1 << 20,
  ) -> np.array:
    s = np.arange(n)
    s[:2] = -1
    i = 0
    while i * i < n - 1:
      i += 1
      if s[i] == i: s[i::i] = i
    return s
  

  def lpf(
    self,
    n: int = 1 << 20,
  ) -> np.array:
    s = np.arange(n)
    s[:2] = -1
    i = 0
    while i * i < n - 1:
      i += 1
      if s[i] != i: continue
      np.minimum(
        s[i::i],
        i,
        out=s[i::i],
      )
    return s