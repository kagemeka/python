import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class Urls():
  start: int
  end: int
  url: str
  expanded_url: str
  display_url: str



@dataclasses.dataclass
class Url():
  urls: typing.List[Urls]



class ConvertUrl():
  def __call__(
    self,
    data: dict,
  ) -> Url:
    self.__url = Url(**data)
    self.__urls()
    return self.__url
  

  def __urls(
    self,
  ) -> typing.NoReturn:
    url = self.__url
    url.urls = [
      Urls(**urls)
      for urls in url.urls
    ]
      


@dataclasses.dataclass
class Hashtag():
  start: int
  end: int
  tag: str



@dataclasses.dataclass
class Description():
  urls: Optional[
    typing.List[Urls]
  ] = None
  hashtags: Optional[
    typing.List[Hashtag]
  ] = None



class ConvertDescription():
  def __call__(
    self,
    data: dict,
  ) -> Description:
    self.__d = Description(
      **data,
    )
    self.__urls()
    self.__hashtags()
    return self.__d
  

  def __urls(
    self,
  ) -> typing.NoReturn:
    d = self.__d
    if d.urls is None: return
    d.urls = [
      Urls(**urls)
      for urls in d.urls
    ]
  

  def __hashtags(
    self,
  ) -> typing.NoReturn:
    d = self.__d
    if d.hashtags is None:
      return
    d.hashtags = [
      Hashtag(**tag)
      for tag in d.hashtags
    ]



@dataclasses.dataclass
class Entities():
  url: Optional[Url] = None
  description: Optional[
    dict
  ] = None



class ConvertEntities():
  def __call__(
    self,
    data: dict,
  ) -> Entities:
    self.__e = Entities(**data)
    self.__url()
    self.__description()
    return self.__e
  

  def __url(
    self,
  ) -> typing.NoReturn:
    e = self.__e
    if e.url is None: return
    e.url = ConvertUrl()(e.url)


  def __description(
    self,
  ) -> typing.NoReturn:
    e = self.__e
    if e.description is None:
      return
    f = ConvertDescription()
    e.description = f(
      e.description,
    )