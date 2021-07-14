import typing
import dataclasses
from dataclasses import (
  astuple,
)


@dataclasses.dataclass
class Color():
  red: int
  green: int
  blue: int


@dataclasses.dataclass
class Palette():
  red: int
  green: int
  blue: int



@typing.final
class ColorFromId:
  __PALETTE: typing.Final[
    Palette
  ] = Palette(
    (1 << 11) - 1, 
    (1 << 15) - 1,
    (1 << 20) - 1,
  )


  def __filter(
    self,
    i: int,
  ) -> int:
    return i ** 2 + 1


  def __call__(
    self, 
    id_: int,
  ) -> Color:
    i = self.__filter(id_)
    p = astuple(self.__PALETTE)
    color = Palette(
      int(x * i % 255)
      for x in p 
    )
    return color 


fn = ColorFromId()
c = fn(1)
print(c)