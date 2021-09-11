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
    assert a[0] == -float('inf')
    for i in range(n):
      j = i + (i & -i)
      if j >= n: continue 
      a[j] = max(a[j], a[i])
    fw = cls(n)
    fw._FenwickTree__a = a
    return fw


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