
import bs4
import dataclasses
import typing


@dataclasses.dataclass
class VoiceActor:
  name: str
  actor_id: int = None 



class ScrapeVoiceActor():

  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> typing.List[VoiceActor]:
    self.__soup = soup
    self.__scrape()
    return self.__actors
  

  def __get_actors_with_id(
    self,
  ) -> typing.NoReturn:
    section = self.__section
    actors = section.find_all(
      'a',
    )
    for actor in actors:
      name = actor.text
      url = actor.get('href')
      id_ = url.split('/')[-2]
      actor = VoiceActor(
        name,
        id_,
      )
      self.__actors.append(
        actor,
      )


  def __get_other_actors(
    self,
  ) -> typing.NoReturn:
    t = self.__section.text
    names = set(
      a.name
      for a in self.__actors
    )
    for name in t.split('、'):
      if name in names:
        continue 
      actor = VoiceActor(name)
      self.__actors.append(
        actor,
      )
    
  
  def __scrape(
    self,
  ) -> typing.NoReturn:
    soup = self.__soup
    self.__actors = []
    section = soup.find(
      class_='cast',
    )
    if section is None: return
    section = section.find(
      'dd',
    )
    self.__section = section
    self.__get_actors_with_id()
    self.__get_other_actors()