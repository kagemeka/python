from kgmk.dsa.algebra.abstract.structure.monoid import (
  Monoid,
)
from \
  kgmk.dsa.tree.misc.segment.normal.one_indexed.topdown \
  .non_recursive \
import (
  SegmentTree,
)

# TODO cut below 

import typing



import typing 

T = typing.TypeVar('T')
class SetPointGetRange(typing.Generic[T]):
  def __init__(
    self,
    monoid: Monoid[T],
    a: typing.List[T],
  ) -> typing.NoReturn:
    self.__seg = SegmentTree(monoid, a)
    self.__monoid = monoid 
  

  def set_point(self, i: int, x: T) -> typing.NoReturn:
    self.__seg[i] = x
  

  def operate_point(self, i: int, x: T) -> typing.NoReturn:
    self.set_point(i, self.__monoid.op(self.get_point(i), x))
  

  def get_point(self, i: int) -> T:
    return self.__seg[i]
  

  def get_range(self, l: int, r: int) -> T:
    return self.__seg.get_range(l, r)