'''Tips
The inversion count of an array is the count of processes in merge-sorting it.

the array should be compressed before calculating the inversion count.
in other words, elments of the array are between 0 and n - 1, here, n is the length of it.
'''
from .fenwick_tree import (
  FenwickTree,
)
from .compress_array import (
  CompressArray,
) 
# TODO cut below



import typing


class InversionCount():
  def __call__(
    self,
    a: typing.List[int],
  ) -> int:
    self.__a = a
    self.__compress()
    self.__calc()
    return self.__cnt


  def __calc(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    n = len(a)
    ft = FenwickTree(n)
    c = 0
    for i in range(n):
      x = a[i]
      c += i - ft.sum(x)
      ft.add(x + 1, 1)
    self.__cnt = c


  def __compress(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    fn = CompressArray()
    self.__a = fn(a)