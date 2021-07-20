from __future__ import (
  annotations,
)
# TODO cut below


import typing



@typing.final
class Modular():

  def __init__(
    self,
    value: int,
    modulo: int,
  ) -> typing.Noreturn:
    self.__value = value
    self.__mod = modulo
    self.__value %= self.mod


  @property
  def mod(self) -> int:
    return self.__mod
  

  def __repr__(self) -> str:
    return f'{self.__value}'
  
  
  def __clone(self) -> Modular:
    return Modular(
      self.__value,
      self.__mod,
    )


  def __to_mod(
    self, 
    rhs: T,
  ) -> Modular:
    if type(rhs) != int:
      return rhs 
    return Modular(
      rhs, 
      self.mod,
    )


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
    return Modular(
      -self.__value,
      self.mod,
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
    return self.inv() * rhs 


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


  def mul_identity(
    self,
  ) -> Modular:
    return Modular(1, self.mod)

    
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