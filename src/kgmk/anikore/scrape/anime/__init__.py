import requests
import bs4
import dataclasses
from dataclasses import (
  astuple,
)
import typing
from typing import (
  Optional,
)
from .metadata import (
  ScrapeMetadata,
  Metadata,
)
from .summary import (
  ScrapeSummary,
  Summary,
)
from .point import (
  ScrapePoint,
  Point,
)
from .tag import (
  Tag,
  ScrapeTags,
)



@dataclasses.dataclass
class Anime():
  anime_id: int
  metadata: Metadata
  summary: Summary
  point: Point
  tags: typing.List[Tag]



class ScrapeAnime():

  def __call__(
    self,
    anime_id: int
  ) -> Anime:
    self.__id = anime_id
    self.__make_soup()
    self.__scrape()
    return self.__anime
  

  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__base_url = (
      'https://www.anikore.jp/'
      'anime/'
    )


  def __make_soup(
    self,
  ) -> typing.NoReturn:
    i = self.__id
    response = requests.get(
      f'{self.__base_url}{i}/',
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    self.__soup = soup 

  
  def __scrape(
    self,
  ) -> typing.NoReturn:
    fns = (
      ScrapeSummary(),
      ScrapePoint(),
      ScrapeMetadata(),
    )
    soup = self.__soup
    id_ = self.__id
    self.__anime = Anime(
      id_,
      *(f(soup) for f in fns),
      ScrapeTags()(id_),
    )