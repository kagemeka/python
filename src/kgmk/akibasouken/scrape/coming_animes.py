from .yearly_anime import (
  ScrapeYearlyAnime,
  YearlyAnime,
)
import bs4 
import dataclasses
import requests
import typing
from datetime import (
  datetime,
)



class ScrapeComingAnimes():

  __SEASON = (
    'winter',
    'spring',
    'summer',
    'autumn',
  )


  def __call__(
    self,
  ) -> typing.Iterator[
    YearlyAnime
  ]:
    self.__make_soup()
    return self.__scrape()    


  def __calc_season(
    self,
  ) -> typing.NoReturn:
    dt = datetime.now()
    i = dt.month // 3 % 4
    season = self.__SEASON[i]
    print(season)
    self.__season = season
  

  def __init__(
    self,
  ) -> typing.NoReturn:
    base_url = (
      'https://'
      'akiba-souken.com/'
      'anime/'
    )
    self.__calc_season()
    season = self.__season
    self.__url = (
      f'{base_url}{season}'
    )
  

  def __make_soup(
    self,
  ) -> typing.NoReturn:
    response = requests.get(
      self.__url,
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    self.__soup = soup

  
  def __scrape(
    self,
  ) -> typing.Iterator[
    YearlyAnime
  ]:
    section = self.__soup.find(
      id='contents',
    )
    animes = section.find_all(
      class_='itemBox',
    )
    get = ScrapeYearlyAnime()
    for anime in animes:
      yield get(anime)