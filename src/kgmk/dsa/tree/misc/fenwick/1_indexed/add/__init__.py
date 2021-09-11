from __future__ import annotations 
import typing 



class FenwickTree():
  @classmethod 
  def from_array(
    cls,
    a: typing.List[int],
  ) -> FenwickTree:
    n = len(a)
    a = a.copy()
    assert a[0] == 0
    for i in range(n):
      j = i + (i & -i)
      if j < n: a[j] += a[i]
    fw = cls(n)
    fw._FenwickTree__a = a
    return fw


  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__a = [0] * (n + 1)
  

  def __setitem__(
    self,
    i: int,
    x: int,
  ) -> typing.NoReturn:
    a = self.__a
    while i < len(a):
      a[i] += x
      i += i & -i
  

  def __getitem__(
    self,
    i: int,
  ) -> int:
    v = 0 
    while i > 0:
      v += self.__a[i]
      i -= i & -i
    return v