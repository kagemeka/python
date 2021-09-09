import typing 



class FenwickTree():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    inf = float('inf')
    self.__a = [-inf] * (n + 1)
  

  def __setitem__(
    self,
    i: int,
    x: int,
  ) -> typing.NoReturn:
    a = self.__a
    while i < len(a):
      a[i] = max(a[i], x)
      i += i & -i
  

  def __getitem__(
    self,
    i: int,
  ) -> int:
    v = -float('inf')
    while i > 0:
      v = max(v, self.__a[i])
      i -= i & -i
    return v