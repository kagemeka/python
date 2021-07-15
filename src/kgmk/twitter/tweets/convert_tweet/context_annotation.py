import typing
import dataclasses
from typing import (
  Optional,
)



@dataclasses.dataclass
class Domain():
  id: str
  name: str
  description: Optional[
    str
  ] = None



@dataclasses.dataclass
class Entity():
  id: str
  name: str
  description: Optional[
    str
  ] = None 



@dataclasses.dataclass
class ContextAnnotation():
  domain: Optional[
    Domain
  ] = None
  entity: Optional[
    Entity
  ] = None



class ConvertContextAnnotation(
):
  def __call__(
    self,
    data: dict,
  ) -> ContextAnnotation:
    self.__data = data
    self.__convert()
    return self.__annot
  

  def __convert(
    self,
  ) -> typing.NoReturn:
    annot = ContextAnnotation(
      **self.__data,
    )
    self.__annot = annot
    self.__domain()
    self.__entity()
  

  def __domain(
    self,
  ) -> typing.NoReturn:
    annot = self.__annot
    dom = annot.domain
    annot.domain = Domain(
      **dom,
    )
  

  def __entity(
    self,
  ) -> typing.NoReturn:
    annot = self.__annot
    ent = annot.entity
    annot.entity = Entity(
      **ent,
    )

