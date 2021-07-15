from .staff import (
  ScrapeStaff,
  Staff,
)

from .voice_actor import (
  ScrapeVoiceActor,
  VoiceActor,
)

from .score import (
  ScrapeScore,
  Score,
)

from .metadata import (
  ScrapeMetadata,
  Metadata,
)

from .studio import (
  ScrapeStudio,
  Studio,
)

from .genre import (
  ScrapeGenre,
  Genre,
)

from .long_text import (
  ScrapeLongText,
  LongText,
)

from .tag import (
  ScrapeTag,
  Tag,
)




import bs4 
import dataclasses
import requests
import typing
from typing import (
  List,
)



@dataclasses.dataclass
class Anime():
  anime_id: int
  staffs: List[Staff]
  voice_actors: List[
    VoiceActor
  ]
  score: Score
  metadata: Metadata
  studios: List[Studio]
  genres: List[Genre]
  long_text: LongText
  tags: List[Tag]



class ScrapeAnime():

  def __call__(
    self,
    anime_id: int,
  ) -> Anime:
    self.__id = anime_id
    self.__make_soup()
    self.__scrape()
    return self.__anime
  

  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__base_url = (
      'https://'
      'akiba-souken.com/'
      'anime/'
    )

  
  def __make_soup(
    self,
  ) -> typing.NoReturn:
    url = self.__base_url
    response = requests.get(
      f'{url}{self.__id}',
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
      ScrapeStaff(),
      ScrapeVoiceActor(),
      ScrapeScore(),
      ScrapeMetadata(),
      ScrapeStudio(),
      ScrapeGenre(),
      ScrapeLongText(),
      ScrapeTag(),
    )
    res = (
      scrape(self.__soup)
      for scrape in scrapes
    )
    self.__anime = Anime(
      self.__id,
      *res,
    )