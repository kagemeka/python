from .emulator import (
  Emulator
)


from abc import (
  ABC,
  abstractmethod,
)


import pyautogui 

import multiprocessing


from .constant import (
  Constant,
)

from .structs import (
  Resolution,
)

from .. import Point


class Runner(ABC):
  def __init__(
      self,
      num_instances: int,
      per_row: int,
      aspect_ratio: float,
      **kwargs):
    
    self.n = num_instances
    self.per_row = per_row

    size = Resolution(
      *pyautogui.size(),
    )
    em_x = size.x / per_row
    em_y = em_x * aspect_ratio
    em_size = Resolution(
      em_x,
      em_y,
    )
    self.em_size = em_size
    self.overhead = \
      Constant.OVERHEAD.value 


  
  def __call__(self):
    self.run()

  
  @abstractmethod
  def run(self):
    ...

  
  def upper_left(self, i):
    r, c = divmod(
      i, 
      self.per_row,
    )
    px, py = self.overhead

    return Point(
      c * self.em_size.x \
        + (c + 1) * px,
      r * self.em_size.y \
         + (r + 1) * py,
    )
  

