import typing


class Fenwick():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__a = [0] * n
  

  def __setitem__(
    self,
    i: int,
    x: int,
  ) -> typing.NoReturn:
    a = self.__a
    while i < len(a):
      a[i] += x
      i |= i + 1


  def __getitem__(
    self,
    i: int,
  ) -> int:
    s = 0 
    while i >= 0:
      s += self.__a[i]
      i &= i + 1
      i -= 1
    return s