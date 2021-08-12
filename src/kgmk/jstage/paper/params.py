import typing 
import dataclasses


@dataclasses.dataclass 
class Params():
  service: typing.Final[int] = 3
  pubyearfrom: typing.Optional[int] = None
  pubyearto: typing.Optional[int] = None
  material: typing.Optional[str] = None
  article: typing.Optional[str] = None
  author: typing.Optional[str] = None
  affil: typing.Optional[str] = None
  keyword: typing.Optional[str] = None
  abst: typing.Optional[str] = None
  text: typing.Optional[str] = None
  issn: typing.Optional[str] = None
  cdjournal: typing.Optional[int] = None
  sortflg: typing.Optional[int] = None
  vol: typing.Optional[int] = None
  no: typing.Optional[int] = None
  start: typing.Optional[int] = None
  count: typing.Optional[int] = None