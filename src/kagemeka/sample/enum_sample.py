from enum import (
  Enum,
  auto,
  unique,
  IntEnum,
  Flag,
  IntFlag,
)
import enum


@unique
class Color(Enum):
  RED = auto() 
  BLUE = auto()
  YELLOW = "yellow"
  CYAN = 3
  GREEN = auto()

  


print(Color.RED.value)
print(Color.GREEN.value)