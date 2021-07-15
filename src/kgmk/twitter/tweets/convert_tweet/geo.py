import typing
from typing import (
  Optional,
)
import dataclasses



@dataclasses.dataclass
class Coordinate():
  latitude: float 
  longitude: float


@dataclasses.dataclass
class Coordinates():
  type: str
  coordinates: Optional[
    typing.List[Coordinate]
  ] = None



class ConvertCoordinates():
  def __call__(
    self,
    data: dict,
  ) -> Coordinates:
    self.__data = data
    self.__convert()
    return self.__coords
  

  def __convert(
    self,
  ) -> typing.NoReturn:
    coords = Coordinates(
      **self.__data,
    )
    self.__coords = coords
    self.__coordinates()
  

  def __coordinates(
    self,
  ) -> typing.NoReturn:
    coords = self.__coords
    ls = coords.coordinates
    if ls is None: return
    coords.coordinates = [
      Coordinate(**x)
      for x in ls
    ]
  


@dataclasses.dataclass
class Geo():
  coordinates: Optional[
    Coordinates
  ] = None
  place_id: Optional[
    str
  ] = None



class ConvertGeo():
  def __call__(
    self,
    data: dict,
  ) -> Geo:
    self.__data = data
    self.__convert()
    return self.__geo


  def __convert(
    self,
  ) -> typing.NoReturn:
    self.__geo = Geo(
      **self.__data,
    )
    self.__coordinates()
  

  def __coordinates(
    self,
  ) -> typing.NoReturn:
    geo = self.__geo
    x = geo.coordinates
    if x is None: return
    f = ConvertCoordinates()
    geo.coordinates = f(x)
    


