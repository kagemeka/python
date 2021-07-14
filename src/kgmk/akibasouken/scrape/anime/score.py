import bs4 
import dataclasses
import typing



@dataclasses.dataclass
class Score():
  satisfaction: float = None
  stroy: float = None
  originality: float = None
  drawing: float = None 
  direction: float = None 
  charactor: float = None 
  voice_actor: float = None 
  sound: float = None 
  song: float = None



class ScrapeScore():

  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Score:
    self.__soup = soup
    self.__scrape()
    return Score(
      *self.__score,
    )

  
  def __scrape(
    self,
  ) -> typing.NoReturn:
    soup = self.__soup
    section = soup.find(
      class_='evalScore',
    )
    scores = []
    total = section.find(
      'strong',
    ).text 
    scores.append(total)
    for s in section.find_all(
      'dd',
    ):
      scores.append(s.text)
    self.__score = (
      None if s == '-' 
      else float(s)
      for s in scores
    ) 
    