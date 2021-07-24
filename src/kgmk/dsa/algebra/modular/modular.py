

from __future__ import (
  annotations,
)
# TODO cut below


import typing
import abc 


class Modular(abc.ABC):
  
  mod: int

  def __init__(
    self,
    value: int,
  ) -> typing.Noreturn:
    value %= self.mod
    self.__value = value


  def __repr__(self) -> str:
    return f'{self.__value}'
  
  
  def __clone(self) -> Modular:
    return self.__class__(
      self.__value,
    )


  @classmethod
  def __to_mod(
    cls, 
    rhs: T,
  ) -> Modular:
    if type(rhs) != int:
      return rhs
    return cls(rhs)


  def __add__(
    self, 
    rhs: T,
  ) -> Modular:
    x = self.__clone()
    rhs = self.__to_mod(rhs)
    x.__value += rhs.__value
    x.__value %= self.mod
    return x
  

  def __iadd__(
    self, 
    rhs: T,
  ) -> Modular:
    return self + rhs


  def __radd__(
    self, 
    lhs: T,
  ) -> Modular:
    return self + lhs
  

  def __neg__(self) -> Modular:
    return self.__class__(
      -self.__value,
    )


  def __sub__(
    self, 
    rhs: T,
  ) -> Modular:
    return self + -rhs
  

  def __isub__(
    self, 
    rhs: T,
  ) -> Modular:
    return self - rhs

  
  def __rsub__(
    self, 
    lhs: T,
  ) -> Modular:
    return -self + lhs


  def __mul__(
    self, 
    rhs: T,
  ) -> Modular:
    x = self.__clone()
    rhs = self.__to_mod(rhs)
    x.__value *= rhs.__value
    x.__value %= self.mod
    return x


  def __imul__(
    self, 
    rhs: T,
  ) -> Modular:
    return self * rhs


  def __rmul__(
    self, 
    lhs: T,
  ) -> Modular:
    return self * lhs
  

  def __truediv__(
    self, 
    rhs: T,
  ) -> Modular:
    rhs = self.__to_mod(rhs)
    return self * rhs.inv()
  

  def __itruediv__(
    self,
    rhs: T,
  ) -> Modular:
    return self / rhs


  def __rtruediv__(
    self,   
    lhs: T,
  ) -> Modular:
    return self.inv() * lhs


  def __pow__(
    self, 
    n: int,
  ) -> Modular:
    return pow(
      self.__value,
      n,
      self.mod,
    )
  

  def __ipow__(
    self, 
    n: int,
  ) -> Modular:
    return self ** n


  def __rpow__(
    self, 
    rhs: T,
  ) -> Modular:
    rhs = self.__to_mod(rhs)
    return rhs ** self.__value


  @classmethod
  def mul_identity(
    cls,
  ) -> Modular:
    return cls(1)
  
  
  @classmethod
  def add_identity(
    cls,
  ) -> Modular:
    return cls(0)
  
    
  def inv(self) -> Modular:
    i = self ** (self.mod - 2)
    return i
  

  def __eq__(
    self, 
    rhs: T,
  ) -> bool:
    rhs = self.__to_mod(rhs)
    return (
      self.__value 
      == rhs.__value
    )


  def congruent(
    self, 
    rhs: T,
  ) -> bool:
    return self == rhs


T: typing.Type = typing.Union[
  int,
  Modular,
]
