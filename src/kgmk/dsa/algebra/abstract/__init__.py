
from abc import (
  ABC,
  abstractmethod,
  abstractclassmethod,
)


from typing import (
  Protocol,
)



class AddSemiGroup(
  Protocol,
):
  

  @abstractmethod
  def __add__(self, other):
    ...



class AddMonoid(
  AddSemiGroup,
  Protocol,
):


  @abstractclassmethod
  def add_identity(
    cls,
  ):
    ...



class AddCommutativeMonoid(
  AddMonoid,
  Protocol,
):

  def __radd__(self, other):
    return self + other


  def add_commutative(
    self,
  ) -> bool:
    return True



class AddGroup(
  AddMonoid,
  Protocol,
): 

  @abstractmethod 
  def add_inv(self):
    ...



class AddAbelianGroup(
  AddGroup,
  Protocol,
):


  def __radd__(self, other):
    return self + other


  def add_commutative(
    self,
  ) -> bool:
    return True

  



class MulSemiGroup(
  Protocol,
):
  

  @abstractmethod
  def __mul__(self, other):
    ...



class MulMonoid(
  MulSemiGroup,
  Protocol,
):


  @abstractclassmethod
  def mul_identity(
    cls,
  ):
    ...



class MulCommutativeMonoid(
  MulMonoid,
  Protocol,
):

  def __rmul__(self, other):
    return self * other


  @property
  def mul_commutative(
    self,
  ) -> bool:
    return True



class MulGroup(
  MulMonoid,
  Protocol,
): 

  @abstractmethod 
  def mul_inv(self):
    ...



class MulAbelianGroup(
  MulGroup,
  Protocol,
):


  def __rmul__(self, other):
    return self * other


  @property
  def mul_commutative(
    self,
  ) -> bool:
    return True






class SemiRing(
  AddCommutativeMonoid,
  MulMonoid,
  Protocol,
):
  ...




class Ring(
  AddAbelianGroup,
  MulMonoid,
  Protocol,
):
  ...




class Field(
  AddAbelianGroup,
  MulGroup,
  Protocol,
):
  ...


