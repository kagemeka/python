import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class UserFields():
  id: bool = True
  name: bool = True
  username: bool = True
  created_at: bool = False
  description: bool = False
  entities: bool = False
  location: bool = False
  pinned_tweet_id: bool = False
  profile_image_url: bool = (
    False
  )
  protected: bool = False
  public_metrics: bool = False
  url: bool = False
  verified: bool = False
  withheld: bool = False


  NAME = 'user.fields'