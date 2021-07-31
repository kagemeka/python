import typing 



class BitCnt():
  
  def __call__(
    self,
    n: int,
  ) -> int:
    a = self.__a
    if n == 0: return 0
    if n in a: return a[n]
    c = self(n // 2) + n % 2
    a[n] = c
    return c
  

  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__a = dict()