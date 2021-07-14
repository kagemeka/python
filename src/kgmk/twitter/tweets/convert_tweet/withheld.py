import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class Withheld():
  copyright: bool
  country_codes: Optional[
    typing.List[str]
  ] = None
  scope: Optional[str] = None
  