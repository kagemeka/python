import typing


class ModCumprod():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.NoReturn:
    for i in range(len(a) - 1):
      a[i + 1] *= a[i]
      a[i + 1] %= self.__mod
  

  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__mod = mod