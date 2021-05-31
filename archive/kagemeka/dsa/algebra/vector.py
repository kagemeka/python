from __future__ import (
  annotations,
)

from enum import Enum 
from dataclasses import (
  dataclass,
  astuple,
  asdict,
  fields,
  make_dataclass,
)

from typing import (
  NamedTuple, 
  Iterable,
  Union,
  Dict,
)

from abc import (
  ABC,
)


from math import (
  sqrt,
)


@dataclass
class Vector(ABC):

  def __iter__(self):
    return iter(astuple(self))
  

  def clone(self):
    return self.__class__(
      *self,
    )

  
  def __add__(self, other):
    x = self.clone()
    for f in fields(x):
      f = f.name
      i = getattr(x, f)
      j = getattr(other, f)
      setattr(x, f, i + j)
    return x


  def __iadd__(self, other):
    return self + other
  
  
  def __neg__(self):
    return self.__class__(*(
      -getattr(self, f.name)
      for f in fields(self)
    ))

  
  def __sub__(self, other):
    return self + -other
  

  def __isub__(self, other):
    return self - other


  def __matmul__(self, other):
    p = 0
    for f in fields(self):
      f = f.name
      i = getattr(self, f)
      j = getattr(other, f)
      p += i * j
    return p
  

  def __mul__(self, r: float):
    x = self.clone()
    for f in fields(x):
      f = f.name
      i = getattr(x, f)
      setattr(x, f, r * i)
    return x
  

  def __imul__(self, r: float):
    return self * r
  

  def __rmul__(self, r: float):
    return self * r 
  

  def __truediv__(
    self,
    r: float,
  ):
    return self * (1 / r)


  def __itruediv__(
    self, 
    r: float,
  ):
    return self / r


  @property
  def norm(self):
    s = sum(
      x ** 2
      for x in
      self.asdict().values()
    )
    return sqrt(s)
    

  @classmethod 
  def define(cls, n):
    vector = make_dataclass(
      cls_name='vector',
      fields=[
        (f'x{i}', float, 0)
        for i in range(n)
      ],
      bases=(cls, ),
    )
    return vector

  
  def asdict(self):
    return asdict(self)



@dataclass
class Vector2D(Vector):
  x: float = 0
  y: float = 0

  def cross(
    self, 
    other,
  ) -> float:
    res = self.x * other.y 
    res -= self.y * other.x
    return res