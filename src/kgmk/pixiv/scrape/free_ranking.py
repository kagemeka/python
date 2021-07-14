from \
  selenium.webdriver \
  .common.by \
import (
  By,
)
from \
  selenium.webdriver.remote \
  .webdriver \
import (
  WebDriver,
)
import dataclasses
import typing
import bs4 
from datetime import (
  datetime,
)
from tqdm import (
  tqdm,
)



@dataclasses.dataclass
class FreeRankedComic():
  comic_id: int
  field: str
  rank: int



@dataclasses.dataclass
class Ranking():
  datetime: datetime
  comics: typing.List[
    FreeRankedComic
  ]



class ScrapeComic():
  
  def __call__(
    self,
    field: str,
    section: bs4.element.Tag,
  ) -> FreeRankedComic:
    self.__field = field 
    self.__section = section
    self.__scrape()
    return self.__comic
  

  def __get_rank(
    self,
  ) -> typing.NoReturn:
    elm = self.__section
    elm = elm.find_element(
      by=By.CLASS_NAME,
      value='jsx-905610923',
    )
    self.__rank = int(elm.text)
  

  def __get_comic_id(
    self,
  ) -> typing.NoReturn:
    elm = self.__section
    url = elm.get_attribute(
      'href',
    )
    self.__comic_id = int(
      url.split('/')[-1],
    )
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__get_rank()
    self.__get_comic_id()
    comic = FreeRankedComic(
      self.__comic_id,
      self.__field,
      self.__rank,
    )
    self.__comic = comic 



class ScrapeFreeRanking():
  
  def __call__(
    self,
  ) -> Ranking:
    self.__scrape()
    return self.__ranking
  

  def __find_fields(
    self,
  ) -> typing.NoReturn:
    driver = self.__driver
    ls = driver.find_elements(
      by=By.CLASS_NAME,
      value=(
        'Menues_menu__p0ouK'
      ),
    )
    self.__fields = ls
  

  def __get_sections(
    self,
  ) -> typing.Iterator[
    bs4.element.Tag
  ]:
    driver = self.__driver
    ls = driver.find_element(
      by=By.CLASS_NAME,
      value=(
        'OfficialWorks_container__eNKQ2'
      ),
    ).find_elements(
      by=By.CLASS_NAME,
      value='OfficialWorkListItem_ranked__2ydPC',
    )
    for section in ls:
      yield section


  def __init__(
    self,
    driver: WebDriver,
  ) -> typing.NoReturn:
    url = (
      'https://comic.pixiv.net'
      '/rankings'
    )
    driver.get(url)
    self.__driver = driver


  def __scrape(
    self,
  ) -> typing.List[
    FreeRankedComic
  ]:
    self.__find_fields()
    fn = ScrapeComic()
    ls = []
    fields = self.__fields
    for field in tqdm(fields):
      field.click()
      s = self.__get_sections()
      for section in s:
        ls.append(fn(
          field.text,
          section,
        ))
    self.__ranking = Ranking(
      datetime.now(),
      ls,
    )