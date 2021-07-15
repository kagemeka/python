from .twitter import (
  ScrapeTwitter,
  Twitter,
)

from .broadcast import (
  ScrapeBroadcast,
  Broadcast,
)

from ..anime import (
  ScrapeAnime,
  Anime,
)


import bs4 
import dataclasses
from dataclasses import (
  astuple,
)
import re
import typing
from typing import (
  Optional,
  List,
)



@dataclasses.dataclass
class YearlyAnime(
  Anime,
):
  twitter: Twitter
  boardcasts: List[Broadcast]


  
class ScrapeYearlyAnime():

  def __call__(
    self,
    section: bs4.element.Tag,
  ) -> YearlyAnime:
    self.__section = section
    self.__scrape()
    return self.__anime
  

  def __get_anime_id(
    self,
  ) -> typing.NoReturn:
    url = self.__section.find(
      class_='mTitle',
    ).find('a').get('href')
    id_ = url.split('/')[-2]
    self.__id = int(id_)


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__get_anime_id()
    anime =  ScrapeAnime()(
      self.__id,
    )
    scrapes = (
      ScrapeTwitter(),
      ScrapeBroadcast(),
    )
    res = (
      scrape(self.__section)
      for scrape in scrapes
    )
    self.__anime = YearlyAnime(
      anime.anime_id,
      anime.staffs,
      anime.voice_actors,
      anime.score,
      anime.metadata,
      anime.studios,
      anime.genres,
      anime.long_text,
      anime.tags,
      *res,
    )