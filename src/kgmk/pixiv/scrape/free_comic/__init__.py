import dataclasses
import typing
import requests
import bs4 
from .metadata import (
  ScrapeMetadata,
  Metadata,
)
from .episode import (
  ScrapeEpisode,
  Episode,
)
from .tag import (
  ScrapeTag,
  Tag,
)
from .summary import (
  ScrapeSummary,
  Summary,
)



@dataclasses.dataclass
class FreeComic():
  comic_id: int
  metadata: Metadata
  summary: Summary
  tags: typing.List[Tag]
  episode: Episode



class ScrapeFreeComic():
  def __call__(
    self,
    comic_id: int,
  ) -> FreeComic:
    self.__id = comic_id
    self.__make_soup()
    self.__scrape()
    return self.__comic    

  
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__base_url = (
      'https://comic.pixiv.net'
      '/works/'
    )


  def __make_soup(
    self,
  ) -> typing.NoReturn:
    base_url = self.__base_url
    id_ = self.__id
    response = requests.get(
      f'{base_url}/{id_}',
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    self.__soup = soup

  
  def __scrape(
    self,
  ) -> typing.NoReturn:
    scrapes = (
      ScrapeMetadata(),
      ScrapeSummary(),
      ScrapeTag(),
      ScrapeEpisode(),
    )
    res = (
      scrape(self.__soup)
      for scrape in scrapes
    )
    self.__comic = FreeComic(
      self.__id,
      *res,
    )