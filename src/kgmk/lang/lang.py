from . import (
  DataClass,
)


#


from enum import (
  Enum,
  auto,
  unique,
)


@unique 
class ISO_639_1(
  Enum,
):
  EN = auto()
  JA = auto()
  ZH = auto()



from dataclasses import (
  dataclass,
)


@dataclass
class Lang(
  DataClass,
):
  name: str
  iso_639_1: ISO_639_1



@dataclass 
class Langs(
  DataClass,
):

  JAPANESE: Lang = Lang(
    name='Japanese',
    iso_639_1=ISO_639_1.JA,
  )

  ENGLISH: Lang = Lang(
    name='English',
    iso_639_1=ISO_639_1.EN,
  )