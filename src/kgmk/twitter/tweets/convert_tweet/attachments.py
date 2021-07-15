import dataclasses
import typing
from typing import (
  Optional,
)


@dataclasses.dataclass
class Attachments():
  media_keys: Optional[
    typing.List[str]
  ] = None
  poll_ids: Optional[
    typing.List[str]
  ] = None
  