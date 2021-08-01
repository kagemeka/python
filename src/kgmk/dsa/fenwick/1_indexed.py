'''Tips
0 := 0...0000
1 := 0...0001
-1 := 1....1111 (inv(1) + 1)
2 := 0...0010
-2 := 1....1110 (inv(2) + 1)

Here, 'inv' means bits world inverse operation.

Fenwick Tree is also known as BIT(Binary Indexed Tree).

default is 1-indexed.
'''
# TODO cut below



import typing



class FenwickTree():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__a = [0] * (n + 1)
  

  def add(
    self,
    i: int,
    x: int,
  ) -> typing.NoReturn:
    a = self.__a; n = len(a)
    while i < n:
      a[i] += x
      i += i & -i
  

  def sum(
    self,
    i: int,
  ) -> int:
    s = 0 
    while i > 0:
      s += self.__a[i]
      i -= i & -i
    return s