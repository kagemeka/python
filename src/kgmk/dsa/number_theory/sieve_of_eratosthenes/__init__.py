import typing


class SieveOfEratorthenes():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> typing.List[bool]:
    s = self.gpf(n)
    for i in range(n):
      s[i] = s[i] == i
    return s


  def gpf(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    s = list(range(n))
    s[0] = s[1] = -1
    i = 0
    while i * i < n - 1:
      i += 1
      if s[i] != i: continue
      for j in range(i, n, i):
        s[j] = i
    return s


  def lpf(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    s = list(range(n))
    s[0] = s[1] = -1
    i = 0
    while i * i < n - 1:
      i += 1
      if s[i] != i: continue
      for j in range(i, n, i):
        if s[j] == j: s[j] = i
    return s
