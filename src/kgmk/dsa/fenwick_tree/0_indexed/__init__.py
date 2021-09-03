import typing


class FenwickTree():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__a = [0] * n
  

  def add(
    self,
    i: int,
    x: int,
  ) -> typing.NoReturn:
    a = self.__a
    while i < len(a):
      a[i] += x
      i |= i + 1


  def sum(
    self,
    i: int,
  ) -> int:
    s = 0 
    while i >= 0:
      s += self.__a[i]
      i &= i + 1
      i -= 1
    return s