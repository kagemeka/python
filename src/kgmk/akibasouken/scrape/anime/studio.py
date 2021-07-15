import bs4 
import dataclasses
import re
import typing



@dataclasses.dataclass 
class Studio():
  name: str
  studio_id: int = None



class ScrapeStudio():

  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> typing.List[Studio]:
    self.__soup = soup
    self.__scrape()
    return self.__studios


  def __find_elms(
    self,
  ) -> typing.NoReturn:
    elms = self.__soup.find(
      class_='info_main',
    ).find_all(
      'dd',
    )[2].find_all('a')
    self.__elms = elms


  def __get_studio(
    self,
    elm: bs4.element.Tag,
  ) -> Studio:
    studio = elm.text
    url = elm.get('href')
    ptn = re.compile(
      r'^.*\?studio=(\d+).*$',
    )
    m = re.match(ptn, url)
    studio_id = int(m.group(1))
    return Studio(
      studio,
      studio_id,
    )


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__find_elms()
    self.__studios = [
      self.__get_studio(elm)
      for elm in self.__elms
    ]