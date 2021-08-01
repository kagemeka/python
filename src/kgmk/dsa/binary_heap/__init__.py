import typing
import heapq


@typing.final
class Heap():
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__a = []


  def __swap(
    self,
    i: int,
    j: int,
  ) -> typing.NoReturn:
    a = self.__a 
    a[i], a[j] = a[j], a[i]


  def push(
    self,
    x: int,
  ) -> typing.NoReturn:
    a = self.__a
    i = len(a)
    a.append(x)
    while i > 0:
      j = (i - 1) // 2
      if a[i] >= a[j]:
        break 
      self.__swap(i, j)
      i = j
    

  def pop(
    self,
  ) -> int:
    a = self.__a 
    self.__swap(0, -1)
    x = a.pop()
    i = 0 
    while 1:
      j = i * 2 + 1
      if j >= len(a) - 1:
        break
      if a[j + 1] < a[j]:
        j += 1
      if a[i] <= a[j]:
        break 
      self.__swap(i, j)
      i = j
    return x

  def __repr__(self) -> str:
    return str(self.__a)
  

  def __bool__(self) -> bool:
    return bool(self.__a)
