import typing



class BitCount():
  def __getitem__(
    self,
    n: int,
  ) -> int:
    return self.__a[n]
  

  def __call__(
    self,
    n: int,
  ) -> int:
    return self.__a[n]
  

  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    a = [0] * n
    for i in range(n):
      a[i] = a[i // 2] + i % 2
    self.__a = a
    