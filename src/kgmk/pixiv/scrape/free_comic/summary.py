import dataclasses
import typing
import bs4 



@dataclasses.dataclass
class Summary():
  overview: str
  follower_cnt: int
  genres: typing.List[str]



class ScrapeSummary():

  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Summary:
    self.__soup = soup
    self.__scrape()
    return self.__summary 


  def __get_overview(
    self,
  ) -> typing.NoReturn:
    elm = self.__soup.find(
      class_='jsx-3803037064',
    )
    self.__overview = elm.text
  

  def __get_follower_cnt(
    self,
  ) -> typing.NoReturn:
    elm = self.__soup.find(
      class_='jsx-736239241',
    )
    self.__follower_cnt = int(
      elm.text.replace(',', '')
    )

  
  def __get_genres(
    self,
  ) -> typing.NoReturn:
    ls = self.__soup.find(
      class_='Introduce_categories__kSPxI',
    ).find_all(
      class_='jsx-1140918973',
    )
    self.__genres = [
      elm.text
      for elm in ls
    ]


  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__get_overview()
    self.__get_follower_cnt()
    self.__get_genres()
    self.__summary = Summary(
      self.__overview,
      self.__follower_cnt,
      self.__genres,
    )