import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class PollFields():
  id: bool = True
  options: bool = True
  duration_minutes: bool = (
    False
  )
  end_datetime: bool = False
  voting_status: bool = False


  NAME = 'poll.fields'