import dataclasses
import typing
import bs4 



@dataclasses.dataclass
class Metadata:
  title: str
  author_text: str
  magazine: str



class ScrapeMetadata(): 
  def __call__(
    self,
    soup: bs4.BeautifulSoup,
  ) -> Metadata:
    self.__soup = soup
    self.__scrape()
    return self.__meta

    
  def __get_txt(
    self,
    cls_: str,
  ) -> str:
    return self.__soup.find(
      class_=cls_,
    ).text 


  def __scrape(
    self,
  ) -> typing.NoReturn:
    classes = (
      'jsx-173046405',
      'jsx-2099034544',
      'jsx-2154117046',
    )
    self.__meta = Metadata(
      *(
        self.__get_txt(cls_)
        for cls_ in classes
      ),
    )