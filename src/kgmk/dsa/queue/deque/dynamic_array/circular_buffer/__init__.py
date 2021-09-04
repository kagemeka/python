import typing


class Deque():
  def __bool__(self) -> bool:
    return self.__l <= self.__r


  def __init__(
    self,
    max_size: int = 1 << 20,
  ) -> typing.NoReturn:
    self.__a = [None] * max_size
    self.__l = 0
    self.__r = -1
  

  def append(
    self,
    v: typing.Any,
  ) -> typing.NoReturn:
    self.__r += 1
    self.__a[self.__r] = v
  

  def appendleft(
    self,
    v: typing.Any,
  ) -> typing.NoReturn:
    self.__l -= 1
    self.__a[self.__l] = v
    

  def empty(self) -> bool:
    return not bool(self)


  def pop(
    self,
  ) -> typing.Any:
    if self.empty(): 
      raise Exception('cannot pop from empty deque.') 
    v = self.__a[self.__r]
    self.__r -= 1
    return v 
  

  def popleft(
    self,
  ) -> typing.Any:
    if self.empty(): 
      raise Exception('cannot pop from empty deque.')
    v = self.__a[self.__l]
    self.__l += 1
    return v