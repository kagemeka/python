from .. import (
  RPA,
  Point,
)

from .structs import (
  Resolution,
)


class Emulator(RPA):
  def __init__(
      self,
      upper_left: Point,
      resolution: Resolution,
      **kwargs,
      ):
    
    self.ul = upper_left 
    self.size = resolution

  
  def click(
      self, 
      button: Point,
      **kwargs):
    button = button.clone()
    button *= self.size 
    button += self.ul 
    super(Emulator, self).click(
      **button.asdict(),
      **kwargs,
    )

  