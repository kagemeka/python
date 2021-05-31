from __future__ import (
  annotations,
)


from ....gen import (
  DataClass,
)

from dataclasses import (
  dataclass,
)

from typing import (
  NoReturn,
)

import numpy as np 

@dataclass
class FrameSz(
  DataClass,
):
  width: int 
  height: int


  def scale(
    self,
    ratio: float,
  ) -> NoReturn:
    self.width = int(
      self.width * ratio,
    )
    self.height = int(
      self.height * ratio,
    )


  def __imul__(
    self,
    ratio: float
  ) -> FrameSz:
    self.scale(
      ratio,
    )
    return self
  

  def __mul__(
    self,
    ratio: float,
  ) -> FrameSz:
    res = FrameSz(
      *self,
    )
    res *= ratio
    return res

  

  @classmethod 
  def from_img(
    cls,
    img: np.ndarray,
  ) -> FrameSz:
    assert img.ndim == 3
    shape = img.shape
    res = cls(
      width=int(shape[1]),
      height=int(shape[0]),
    )
    return res 
