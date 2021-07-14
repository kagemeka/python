import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class Expansions():
  pinned_tweet_id: bool = False

  NAME = 'expansions'