import bs4 
import dataclasses
import re
import typing
from typing import (
  Optional,
)
from datetime import (
  datetime,
)
from unicodedata import (
  normalize,
)


@dataclasses.dataclass 
class Metadata():
  title: str 
  media: str
  year: int
  season: Optional[int] = None
  date: Optional[
    datetime.date
  ] = None 
  official_site: Optional[
    str
  ] = None
  copyright_: Optional[str] = (
    None
  )
  


class ScrapeMetadata():

  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Metadata:
    self.__soup = soup 
    self.__scrape()
    return self.__meta

  
  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__get_title_media()
    self.__get_year_season()
    self.__get_date()
    self.__get_official_site()
    self.__get_copyright()
    self.__meta = Metadata(
      self.__title,
      self.__media,
      self.__year,
      self.__season,
      self.__date,
      self.__official_site,
      self.__copyright,
    )
  

  def __get_title_media(
    self,
  ) -> typing.NoReturn:
    section = self.__soup.find(
      class_='itemTitle',
    )
    title = section.find(
      'h1',
    ).text
    media = section.find(
      class_='category',
    ).text
    self.__title = title
    self.__media = media


  def __get_year_season(
    self,
  ) -> typing.NoReturn:
    section = self.__soup.find(
      class_='info_main',
    )
    url = section.find(
      'dd',
    ).find('a').get('href')
    ptn = re.compile(
      r'^.*season=(\d+).*$',
    )
    m = re.match(ptn, url)
    self.__season = (
      m.group(1) if m else None
    )
    ptn = re.compile(
      r'^.*year=(\d+).*$',
    )
    m = re.match(ptn, url)
    self.__year = (
      m.group(1) if m else None
    )
  
  
  def __get_date(
    self,
  ) -> typing.NoReturn:
    s = self.__soup.find(
      class_='info_main',
    ).find_all('dd')[1].text
    s = normalize('NFKD', s)
    s = s.rstrip('~')
    try:
      dt = datetime.strptime(
        s,
        '%Y年%m月%d日'
      )
      self.__date = dt.date()
    except:
      self.__date = None
      

  def __get_official_site(
    self,
  ) -> typing.NoReturn:
    elm = self.__soup.find(
      class_='specBox',
    ).find('a')
    url = (
      elm.get('href') if elm
      else None 
    )
    self.__official_site = url

  
  def __get_copyright(
    self,
  ) -> typing.NoReturn:
    elm = self.__soup.find(
      class_='copyright',
    )
    self.__copyright = (
      elm.text if elm else None
    )