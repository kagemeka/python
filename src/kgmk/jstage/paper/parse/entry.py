import typing 
import dataclasses
import datetime
from .author import (
  Author,
)



@dataclasses.dataclass 
class ArticleTitle():
  en: str
  ja: str 



@dataclasses.dataclass 
class ArticleLink():
  en: str
  ja: str



@dataclasses.dataclass 
class MaterialTitle():
  en: str 
  ja: str 



@dataclasses.dataclass 
class Entry():
  article_title: ArticleTitle
  article_link: ArticleLink
  cdjournal: str
  material_title: MaterialTitle
  prism_issn: typing.Optional[str]
  prism_eissn: str
  prism_volume: int
  prism_number: int
  prism_starting_page: int
  prism_ending_page: int
  pubyear: int
  prism_doi: str
  systemcode: int 
  systemname: str
  title: str
  link: str 
  id: str 
  updated: datetime.datetime
  author: typing.Optional[Author] = None
  joi: typing.Optional[str] = None
  cdvols: typing.Optional[int] = None


from dataclasses import fields

class Parse():
  def __call__(
    self,
    data: dict,
  ) -> Entry:
    self.__data = data 
    self.__parse()
    return self.__entry
  

  def __parse(
    self,
  ) -> typing.NoReturn:
    data = self.__data 
    key = {
      'article_title': 'article_title',
      'article_link': 'article_link',
      'author': 'author',
      'cdjournal': 'cdjournal',
      'material_title': 'material_title',
      'prism_issn': 'prism:issn',
      'prism_eissn': 'prism:eIssn',
      'prism_volume': 'prism:volume',
      'prism_number': 'prism:number',
      'prism_starting_page': 'prism:startingPage',
      'prism_ending_page': 'prism:endingPage',
      'pubyear': 'pubyear',
      'prism_doi': 'prism:doi',
      'systemcode': 'systemcode',
      'systemname': 'systemname',
      'title': 'title',
      'link': 'link',
      'id': 'id',
      'updated': 'updated',
      'joi': 'joi',
      'cdvols': 'cdvols',
    }
    self.__entry = Entry(**{
      f.name: data.get(
        key[f.name],
        None,
      )
      for f in dataclasses.fields(Entry)
    })
    self.__article_title()
    self.__article_link()
    self.__author()
    self.__material_title()
    self.__link()
    self.__updated()
    self.__int_fields()
  

  def __article_title(
    self,
  ) -> typing.NoReturn:
    e = self.__entry
    ttl = ArticleTitle(
      **e.article_title,
    )
    e.article_title = ttl
  

  def __article_link(
    self,
  ) -> typing.NoReturn:
    e = self.__entry
    link = ArticleLink(
      **e.article_link,
    )
    e.article_link = link 
  

  def __author(
    self,
  ) -> typing.NoReturn:
    from .author import Parse
    e = self.__entry
    e.author = Parse()(e.author)
  

  def __material_title(
    self,
  ) -> typing.NoReturn:
    e = self.__entry
    ttl = MaterialTitle(
      **e.material_title,
    )
    e.material_title = ttl
  

  def __link(
    self,
  ) -> typing.NoReturn:
    e = self.__entry 
    e.link = e.link['@href']
  

  def __updated(
    self,
  ) -> typing.NoReturn:
    from datetime import (
      datetime,
    )
    e = self.__entry
    dt = datetime.strptime(
      e.updated.split('+')[0],
      '%Y-%m-%dT%H:%M',
    )
    e.updated = dt


  def __int_fields(
    self,
  ) -> typing.NoReturn:
    e = self.__entry
    for f in dataclasses.fields(e):
      f = f.name 
      try:
        setattr(
          e, 
          f,
          int(getattr(e, f)),
        )
      except:
        pass 