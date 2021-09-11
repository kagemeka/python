from kgmk.dsa.tree.misc.fenwick.one_indexed.add import (
  FenwickTree,
)

# TODO cut below
import typing 

class RangeAddRangeSum():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__fw0 = FenwickTree(n)
    self.__fw1 = FenwickTree(n)


  def __setitem__(
    self,
    lr: typing.Tuple[int, int],
    x: int,
  ) -> typing.NoReturn:
    l, r = lr 
    r += 1
    self.__fw0[l] = -x * l 
    self.__fw0[r] = x * r 
    self.__fw1[l] = x 
    self.__fw1[r] = -x 
  

  def __getitem__(
    self,
    i: typing.Tuple[int, int],
  ) -> int:
    i += 1
    return self.__fw0[i] + self.__fw1[i] * i
  

  def get_range(
    self,
    l: int,
    r: int,
  ) -> int:
    return -self[l - 1] + self[r]
