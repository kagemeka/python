import typing
from .modular import (
  Modular,
)



class ModFactory():
  def __call__(
    self,
    modulo: int,
  ) -> Modular:
    class Mint(Modular):
      mod: typing.Final[
        int
      ] = modulo
    return Mint 
