import typing 
import dataclasses


# TODO get paper list
@dataclasses.dataclass 
class Params():
  service: typing.Final[int] = 2
  pubyearfrom: typing.Optional[int] = None
  pubyearto: typing.Optional[int] = None
  material: typing.Optional[str] = None
  issn: typing.Optional[str] = None
  cdjournal: typing.Optional[int] = None
  volorder: typing.Optional[int] = None

