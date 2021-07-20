import typing
from .modular import (
  Modular,
)



class ModFactory():
  def __call__(
    self,
    value: int,
  ) -> Modular:
    mod = self.mod
    return Modular(value, mod)
    

  def __init__(
    self,
    modulo: int,
  ) -> typing.NoReturn:
    self.__mod = modulo


  @property
  def mod(self) -> int:
    return self.__mod