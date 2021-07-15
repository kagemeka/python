import bs4 
import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class Twitter():
  username: Optional[str] = (
    None
  )


class ScrapeTwitter():
  
  def __call__(
    self,
    section: bs4.element.Tag,
  ) -> Twitter:
    self.__section = section
    self.__scrape()
    return self.__twitter
  
  
  def __get_url(
    self,
  ) -> typing.NoReturn:
    elm = self.__section.find(
      class_='officialTwitter',
    )
    self.__url = (
      elm.get('href') if elm
      else None
    )
  

  def __get_username(
    self,
  ) -> typing.NoReturn:
    self.__username = (
      self.__url.split('/')[-1]
      if self.__url else None
    )


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__get_url()
    self.__get_username()
    self.__twitter = Twitter(
      self.__username,
    )