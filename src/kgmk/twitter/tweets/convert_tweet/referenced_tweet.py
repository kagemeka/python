import typing
import dataclasses
from typing import (
  Optional,
)



@dataclasses.dataclass
class ReferencedTweet():
  type: str
  id: str