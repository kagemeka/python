import typing


class SieveOfEratosthenes():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    s = self.lpf(n)
    for i in range(n):
      s[i] = s[i] == i
    return s


  def lpf(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    s = list(range(n))
    s[0] = s[1] = -1
    i = 0 
    while i * i < n:
      i += 1
      if s[i] != i: continue
      for j in range(
        i * 2,
        n,
        i,
      ): s[j] = i
    return s 


  def spf(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    s = list(range(n))
    s[0] = s[1] = -1
    i = 0 
    while i * i < n:
      i += 1
      if s[i] != i: continue
      for j in range(
        i * 2,
        n,
        i,
      ): 
        if s[j] == j: s[j] = i
    return s 