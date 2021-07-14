import dataclasses
import typing
import bs4 
import re



@dataclasses.dataclass
class Tag():
  name: str
  cnt: int



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
    ls = self.__soup.find(
      class_='Introduce_tags__1PIdO',
    ).find_all(
      class_='jsx-1448592460',
    )
    ptn = re.compile(
      r'^#(.*)\((\d+)\)$',
    )
    tags = []
    for elm in ls:
      elm = ''.join(
        elm.text.split(),
      )
      m = re.match(ptn, elm)
      name = m.group(1)
      cnt = int(m.group(2))
      tag = Tag(name, cnt)
      tags.append(tag)
    self.__tags = tags