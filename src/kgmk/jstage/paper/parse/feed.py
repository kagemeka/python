import typing 
import dataclasses
import datetime
from .entry import Entry



@dataclasses.dataclass 
class Result:
  status: str
  message: typing.Optional[str] = None



@dataclasses.dataclass 
class Feed():
  result: Result
  link: str
  id: str
  updated: datetime.datetime
  start_index: int
  items_per_page: int
  entry: typing.List[Entry]
  total_results: typing.Optional[int] = None
  title: str = 'Articles'
  servicecd: int = 3


from dataclasses import fields

class Parse():
  
  def __call__(
    self,
    data: dict,
  ) -> Feed:
    self.__data = data
    self.__parse()
    return self.__feed 
  

  def __parse(
    self,
  ) -> typing.NoReturn:
    data = self.__data
    key = {
      'result': 'result',
      'link': 'link',
      'id': 'id',
      'updated': 'updated',
      'total_results': (
        'opensearch:'
        'totalResults'
      ),
      'start_index': (
        'opensearch:'
        'startIndex'
      ),
      'items_per_page': (
        'opensearch:'
        'itemsPerPage'
      ),
      'title': 'title',
      'servicecd': 'servicecd',
      'entry': 'entry',
    }
    f = Feed(**{
      f.name: data[key[f.name]]
      for f in fields(Feed)
    })
    self.__feed = f
    self.__result()
    self.__link()
    self.__updated()
    if not f.items_per_page:
      return
    self.__entry()
    self.__int_fields()
  

  def __entry(
    self,
  ) -> typing.NoReturn:
    from .entry import Parse
    f = self.__feed 
    if type(f.entry) != list:
      f.entry =[f.entry]
    f.entry = [
      Parse()(e)
      for e in f.entry
    ]


  def __result(
    self,
  ) -> typing.NoReturn:
    f = self.__feed 
    f.result = Result(
      **f.result,
    )


  def __link(
    self,
  ) -> typing.NoReturn:
    f = self.__feed
    f.link = f.link['@href']
  
  
  def __updated(
    self,
  ) -> typing.NoReturn:
    from datetime import (
      datetime,
    )
    f = self.__feed
    dt = datetime.strptime(
      f.updated.split('+')[0],
      '%Y-%m-%dT%H:%M',
    )
    f.updated = dt


  def __int_fields(
    self,
  ) -> typing.NoReturn:
    f = self.__feed
    f.total_results = int(
      f.total_results,
    )
    f.start_index = int(
      f.start_index,
    )
    f.items_per_page = int(
      f.items_per_page,
    )