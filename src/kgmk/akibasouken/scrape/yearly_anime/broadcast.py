import bs4 
import dataclasses
import re
import typing
from typing import (
  Optional,
)


@dataclasses.dataclass
class Broadcast():
  channel: str
  schedule: Optional[str] = (
    None
  )
  url: Optional[str] = None



class ScrapeBroadcast():

  def __call__(
    self,
    section: bs4.element.Tag,
  ) -> typing.List[Broadcast]:
    self.__section = section
    self.__scrape()
    return self.__broadcasts
  

  def __get_streams(
    self,
  ) -> typing.NoReturn:
    elm = self.__section.find(
      class_='dogaLink',
    )
    if elm is None: return
    for a in elm.find_all('a'):
      channel = a.text
      bc = Broadcast(channel)
      self.__broadcasts.append(
        bc,
      )


  def __get_others(
    self,
  ) -> typing.NoReturn:
    elm = self.__section.find(
      class_='schedule',
    )
    if elm is None: return
    elms = elm.find_all('td')
    for elm in elms:
      self.__get_unit(elm)
 

  def __get_unit(
    self,
    elm: bs4.element.Tag,
  ) -> Broadcast:
    elms = elm.find_all('span')
    if not elms: return
    channel = elms[0].text
    schedule = (
      None if len(elms) < 2
      else elms[1].text
    )
    bc = Broadcast(
      channel,
      schedule,
    )
    self.__broadcasts.append(
      bc,
    )


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__broadcasts = []
    self.__get_streams()
    self.__get_others()