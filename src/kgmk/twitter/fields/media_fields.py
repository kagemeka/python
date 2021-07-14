import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class MediaFields():
  media_key: bool = True
  type: bool = True
  duration_ms: bool = False
  height: bool = False
  non_public_metrics: bool = (
    False
  )
  organic_metrics: bool = False
  preview_iamge_url: bool = (
    False
  )
  promoted_metrics: bool = (
    False
  )
  public_metrics: bool = False
  width: bool = False


  NAME = 'media.fields'