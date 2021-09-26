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
    n = 1 << (len(a)- 1).bit_length()
    seg = [None] * (n << 1)
    seg[n:n + len(a)] = a.copy()
    for i in range(n + len(a), n << 1): seg[i] = monoid.e()
    self.__a = seg
    for i in range(n - 1, 0, -1): self.__update(i)
 

  def __len__(self) -> int: return len(self.__a) >> 1
  def __repr__(self) -> str: return str(self.__a)


  def __getitem__(
    self, 
    i: typing.Union[typing.Tuple[int, int], int],
  ) -> T:
    if type(i) == int:
      return self.__a[i + len(self)]
    l, r = i
    return self.__get(l, r, 0, len(self), 1)
  

  def __get(self, l: int, r: int, s: int, t: int, i: int) -> T:
    m = self.__monoid
    if t <= l or r <= s: return m.e()
    if l <= s and t <= r: return self.__a[i]
    c = (s + t) // 2
    return m.op(
      self.__get(l, r, s, c, i << 1),
      self.__get(l, r, c, t, i << 1 | 1),
    )


  def __setitem__(self, i: int, x: T) -> typing.NoReturn:
    i += len(self)
    self.__a[i] = x
    while i > 1:
      i >>= 1
      self.__update(i)


  def __update(self, i: int) -> typing.NoReturn:
    a = self.__a
    a[i] = self.__monoid.op(a[i << 1], a[i << 1 | 1]) 
