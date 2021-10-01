from kgmk.dsa.algebra.abstract.structure.monoid import (
  Monoid,
)

# TODO cut below 

from __future__ import annotations
import typing



T = typing.TypeVar('T')
class SegmentTree(typing.Generic[T]):
  def __init__(
    self,
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
  def __repr__(self) -> str: return str(self.__a)from __future__ import (
  annotations,
)
import typing
import dataclasses



T = typing.TypeVar('T')
@dataclasses.dataclass
class Monoid(
  typing.Generic[T],
):
  fn: typing.Callable[
    [T, T],
    T,
  ]
  e: typing.Callable[[], T]



T = typing.TypeVar('T')
class SegTree(
  typing.Generic[T],
):
  def __getitem__(
    self,
    lr: typing.Union[
      typing.Tuple[int, int],
      int,
    ],
  ) -> T:
    if type(lr) == int:
      return self.__a[
        lr + self.__n
      ]
    m = self.__m 
    l, r = self.__l, self.__r 
    i = self.__i
    ql, qr = lr
    if qr <= l or r <= ql:
      return m.e()
    if ql <= l and r <= qr:
      return self.__a[i]
    c = (l + r) // 2
    self.__i = i << 1
    self.__r = c
    lhs = self[lr]
    self.__i = i << 1 | 1
    self.__l, self.__r = c, r
    rhs = self[lr]
    self.__l, self.__i = l, i
    return m.fn(lhs, rhs)



  def __init__(
    self,
    monoid: Monoid[T],
    n: int,
  ) -> typing.NoReturn:
    self.__m = monoid
    n = (n - 1).bit_length()
    self.__n = n = 1 << n
    self.__a = [
      monoid.e() 
      for _ in range(n << 1)
    ]
    self.__l, self.__r = 0, n
    self.__i = 1


  def __len__(self) -> int:
    return self.__n


  def __repr__(self) -> str:
    return str(self.__a)


  def __setitem__(
    self,
    i: int,
    x: T,
  ) -> typing.NoReturn:
    i += self.__n
    self.__a[i] = x; i >>= 1
    while i:
      self.__update(i)
      i >>= 1
  
  
  def __update(
    self,
    i: int,
  ) -> typing.NoReturn:
    a = self.__a
    a[i] = self.__m.fn(
      a[i << 1],
      a[i << 1 | 1],
    ) 


  @classmethod
  def from_array(
    cls,
    monoid: Monoid,
    arr: typing.List[int],
  ) -> SegTree:
    n = len(arr)
    seg = cls(monoid, n)
    for i in range(n):
      seg[i] = arr[i]
    return seg  



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
