from __future__ import annotations 
from kgmk.dsa.algebra.abstract.structure.monoid import (
  Monoid,
)


# TODO cut below 

import typing 



T = typing.TypeVar('T')
class FenwickTree(typing.Generic[T]):
  def __init__(
    self,
    monoid: Monoid[T],
    a: typing.List[T],
  ) -> FenwickTree[T]:
    n = len(a)
    fw = [None] * (n + 1)
    fw[1:] = a.copy()
    for i in range(1, n + 1):
      j = i + (i & -i)
      if j >= n + 1: continue
      fw[j] = monoid.op(fw[j], fw[i])
    self.__a = fw


  def __getitem__(self, i: int) -> T:
    m = self.__monoid 
    v = m.e()
    while i > 0:
      v = m.op(v, self.__a[i])
      i -= i & -i
    return v
  

  def __setitem__(self, i: int, x: T) -> typing.NoReturn:
    a = self.__a
    while i < len(a):
      a[i] = self.__monoid.op(a[i], x)
      i += i & -i