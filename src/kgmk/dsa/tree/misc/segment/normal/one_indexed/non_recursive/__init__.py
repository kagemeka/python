from kgmk.dsa.algebra.abstract.structure.monoid import (
  Monoid,
)

# TODO cut below 

from __future__ import annotations
import typing



T = typing.TypeVar('T')
class SegmentTree(typing.Generic[T]):
  def __init__(self,
    monoid: Monoid[T],
    a: typing.List[T],
  ) -> typing.NoReturn:
    self.__monoid = monoid
    n = len(a)
    seg = [None] * (n << 1)
    seg[n:] = a.copy()
    self.__a = seg
    for i in range(n - 1, 0, -1): self.__update(i)
 

  def __len__(self) -> int: return len(self.__a) >> 1
  def __repr__(self) -> str: return str(self.__a)


  def __getitem__(self, i: int) -> T:
    return self.__a[i + len(self)]


  def get_range(self, l: int, r: int) -> T:
    a = self.__a
    m = self.__monoid
    n = len(self)
    l, r = l + n, r + n
    vl = vr = m.e()
    while l < r:
      if l & 1:
        vl = m.op(vl, a[l])
        l += 1
      if r & 1:
        r -= 1
        vr = m.op(a[r], vr)
      l, r = l >> 1, r >> 1
    return m.op(vl, vr)    


  def __setitem__(self, i: int, x: T) -> typing.NoReturn:
    i += len(self)
    self.__a[i] = x
    while i > 1:
      i >>= 1
      self.__update(i)


  def __update(self, i: int) -> typing.NoReturn:
    a = self.__a
    a[i] = self.__monoid.op(a[i << 1], a[i << 1 | 1]) 