import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class PlaceFields():
  full_name: bool = True
  id: bool = True
  contained_within: bool = (
    False
  )
  country: bool = False
  country_code: bool = False
  geo: bool = False
  name: bool = False
  place_type: bool = False
  

  NAME = 'place.fields'