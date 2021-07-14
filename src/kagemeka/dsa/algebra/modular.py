from __future__ import (
  annotations,
)

from enum import Enum


class Modulus(Enum):
  MOD0 = 10**4 + 7
  MOD1 = 998_244_353
  MOD2 = 10**9 + 7
  MOD3 = 10**9 + 9


# cut below


from abc import (
  ABC,
)


class Modular(ABC):
  mod: int = None
  

  def __init__(
    self,
    value: int,
  ):
    value %= self.mod
    self.value = value
  

  def __repr__(
    self,
  ):
    return f'{self.value}'
  
  
  def clone(
    self,
  ):
    return self.__class__(
      self.value,
    )


  @classmethod
  def modularize(
    cls, 
    other,
  ):
    if type(other) == int:
      return cls(other)
    return other


  def __add__(self, other):
    x = self.clone()
    other = self.modularize(
      other,
    )
    x.value += other.value
    x.value %= self.mod
    return x
  

  def __iadd__(self, other):
    return self + other


  def __radd__(self, other):
    return self + other
  

  def __neg__(self):
    return self.__class__(
      -self.value,
    )


  def __sub__(self, other):
    return self + -other
  

  def __isub__(self, other):
    return self - other

  
  def __rsub__(self, other):
    return -self + other 


  def __mul__(self, other):
    x = self.clone()
    other = self.modularize(
      other,
    )
    x.value *= other.value
    x.value %= self.mod
    return x


  def __imul__(self, other):
    return self * other


  def __rmul__(self, other):
    return self * other
  

  def __truediv__(self, other):
    other = self.modularize(
      other,
    )
    return self * other.inv()
  

  def __itruediv__(
    self,
    other,
  ):
    return self / other


  def __rtruediv__(
    self,   
    other,
  ):
    return self.inv() * other 


  def __pow__(self, n: int):
    if n == 0:
      e = self.mul_identity()
      return e
    a = self ** (n >> 1)
    a *= a
    if n & 1: a *= self
    return a
  

  def __ipow__(self, n: int):
    return self ** n


  def __rpow__(self, other):
    other = self.modularize(
      other,
    )
    return other ** self.value


  @classmethod
  def mul_identity(cls):
    return cls(1)

    
  def inv(self):
    i = self ** (self.mod - 2)
    return i
  

  def __eq__(self, other):
    other = self.modularize(
      other,
    )
    return (
      self.value == other.value
    )


  def congruent(
    self, 
    other,
  ):
    return self == other
  

  def factorial(
    self, 
  ):
    n = self.value
    fact = [
      self.__class__(i)
      for i in range(n)
    ]
    fact = np.array(fact)
    e = self.mul_identity()
    fact[0] = e
    fact.cumprod(out=fact)
    return fact
  

  def inv_factorial(
    self,
  ): 
    fact = self.factorial()
    n = self.value
    ifact = np.arange(
      1, 
      n + 1,
    ).astype(object)
    ifact[-1] = fact[-1].inv()
    ifact[::-1].cumprod(
      out=ifact[::-1],
    )
    return ifact
      

  @classmethod
  def define(
    cls,
    mod: int,
  ):
    class NewModular(
      Modular,
    ):
      pass
    NewModular.mod = mod
    return NewModular