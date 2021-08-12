import typing 
import dataclasses
import datetime

from .feed import Feed


@dataclasses.dataclass 
class Paper():
  feed: Feed


import requests



class Parse():
  def __call__(
    self,
    response: requests.models.Response,
  ) -> Paper:
    self.__r = response
    self.__parse()
    return self.__paper
  

  def __parse(
    self,
  ) -> typing.NoReturn:
    import xmltodict
    r = xmltodict.parse(
      self.__r.content,
    )
    p = Paper(**r)
    self.__paper = p
    self.__feed()
  

  def __feed(
    self,
  ) -> typing.NoReturn:
    p = self.__paper
    from .feed import Parse
    p.feed = Parse()(p.feed)
