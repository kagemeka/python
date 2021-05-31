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




@dataclass 
class Segment2D:
  p0: Vector2D
  p1: Vector2D 


  def intersect(
    self,
    other: Segment2D,
  ) -> bool:
    return (
      self.across(other)
      & other.across(self)
    )
  

  def across(
    self,
    other: Segment2D,
  ) -> bool:
    v0 = other.p1 - other.p0
    v1 = self.p0 - other.p0 
    v2 = self.p1 - other.p0
    c0 = v0.cross(v1)
    c1 = v0.cross(v2)
    return c0 * c1 <= 0