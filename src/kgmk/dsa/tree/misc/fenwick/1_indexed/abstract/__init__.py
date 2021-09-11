from __future__ import annotations 
from kgmk.dsa.algebra.abstract.monoid import (
  Monoid,
)


# TODO cut below 

import typing 



T = typing.TypeVar('T')
class FenwickTree(typing.Generic[T]):
  @classmethod 
  def from_array(
    cls,
    monoid: Monoid[T],
    a: typing.List[T],
  ) -> FenwickTree[T]:
    n = len(a)
    a = a.copy()
    assert a[0] == monoid.e()
    for i in range(n):
      j = i + (i & -i)
      if j >= n: continue
      a[j] = monoid.fn(a[j], a[i])
    fw = cls(monoid, n)
    fw._FenwickTree__a = a
    return fw


  def __getitem__(
    self,
    i: int,
  ) -> T:
    m = self.__monoid 
    v = m.e()
    while i > 0:
      v = m.fn(v, self.__a[i])
      i -= i & -i
    return v


  def __init__(
    self,
    monoid: Monoid[T],
    n: int,
  ) -> typing.NoReturn:
    assert monoid.commutative 
    self.__a = [monoid.e() for _ in range(n + 1)]
    self.__monoid = monoid 
  

  def __setitem__(
    self,
    i: int,
    x: T,
  ) -> typing.NoReturn:
    a = self.__a
    while i < len(a):
      a[i] = self.__monoid.fn(a[i], x)
      i += i & -i