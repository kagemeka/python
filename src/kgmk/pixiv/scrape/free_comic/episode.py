import dataclasses
import typing
import bs4 
from datetime import (
  datetime,
)



@dataclasses.dataclass
class Episode:
  latest_update: datetime
  oldest_update: datetime
  display_cnt: int



class ScrapeEpisode():
  
  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Episode:
    self.__soup = soup
    self.__scrape()
    return self.__episode


  def __find_elements(
    self,
  ) -> typing.NoReturn:
    elms = self.__soup.find(
      class_='Episodes_container__1_X7w',
    ).find_all(
      class_='Episodes_storyWrapper__1rPiM',
    )
    self.__elms = elms
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__find_elements()
    elms = self.__elms
    cnt = len(elms)
    dates = []
    for elm in elms:
      date = elm.find(
        class_='jsx-1662019296',
      ).text
      date = ''.join(
        date.split(),
      ).lstrip('更新日:')
      dt = datetime.strptime(
        date, '%Y年%m月%d日',
      )
      dates.append(dt.date())
    dates.sort()
    oldest = dates[0]
    latest = dates[-1]
    self.__episode = Episode(
      latest,
      oldest,
      cnt,
    )