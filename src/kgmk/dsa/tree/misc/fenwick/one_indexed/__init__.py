from kgmk.dsa.algebra.abstract.structure.monoid import Monoid


# TODO cut below 

import typing 



S = typing.TypeVar('S')
class FenwickTree(typing.Generic[S]):
  def __init__(
    self,
    monoid: Monoid[S],
    a: typing.List[S],
  ) -> typing.NoReturn:
    n = len(a)
    fw = [None] * (n + 1)
    fw[1:] = a.copy()
    for i in range(1, n + 1):
      j = i + (i & -i)
      if j < n + 1: fw[j] = monoid.op(fw[j], fw[i])
    self.__data = fw


  def __setitem__(self, i: int, x: S) -> typing.NoReturn:
    d = self.__data
    size = len(d) - 1
    assert 0 <= i < size
    i += 1
    while i < size + 1:
      d[i] = self.__monoid.op(d[i], x)
      i += i & -i


  def __getitem__(self, i: int) -> S:
    m, d = self.__monoid, self.__data
    assert 0 <= i < len(d)
    v = m.e()
    while i > 0:
      v = m.op(v, d[i])
      i -= i & -i
    return v