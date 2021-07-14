
import bs4 
import dataclasses
import typing



@dataclasses.dataclass
class Tag():
  name: str



class ScrapeTag():
  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> typing.List[Tag]:
    self.__soup = soup
    self.__scrape()
    return self.__tags
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    elms = self.__soup.find(
      class_='tag',
    ).find_all('a')[:-1]
    self.__tags = [
      Tag(elm.text)
      for elm in elms
    ]