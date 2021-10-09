import typing


class Fenwick():
  def __init__(self, n: int) -> typing.NoReturn:
    self.__data = [0] * n
  

  def __setitem__(self, i: int, x: int) -> typing.NoReturn:
    d = self.__data
    while i < len(d):
      d[i] += x
      i |= i + 1


  def __getitem__(self, i: int) -> int:
    s = 0 
    while i >= 0:
      s += self.__d[i]
      i &= i + 1
      i -= 1
    return s