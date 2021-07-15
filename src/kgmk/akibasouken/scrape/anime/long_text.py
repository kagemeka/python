import bs4 
import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class LongText():
  commentary: Optional[str] = (
    None
  )
  overview: Optional[str] = (
    None
  )



class ScrapeLongText():

  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> LongText:
    self.__soup = soup
    self.__scrape()
    return self.__long_txt
  

  def __get_commentary(
    self,
  ) -> typing.NoReturn:
    elm = self.__soup.find(
      class_='commentary',
    )
    self.__commentary = (
      elm.text if elm else None
    )

  
  def __get_overview(
    self,
  ) -> typing.NoReturn:
    elm = self.__soup.find(
      class_='storyLine',
    )
    self.__overview = (
      elm.text if elm else None
    )
      

  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__get_commentary()
    self.__get_overview()
    self.__long_txt = LongText(
      self.__commentary,
      self.__overview,
    )