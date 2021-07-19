from __future__ import (
  annotations,
)


from ..algebra.vector import (
  Vector2D,
)


from dataclasses import (
  dataclass,
)


@dataclass 
class Triangle:
  p0: Vector2D
  p1: Vector2D
  p2: Vector2D


  @property
  def area(
    self, 
    signed=True,
  ):
    return abs(
      self.signed_area,
    )

  
  @property
  def signed_area(
    self,
  ):
    p1 = self.p1 - self.p0 
    p2 = self.p2 - self.p0
    return p1.cross(p2) / 2
    

