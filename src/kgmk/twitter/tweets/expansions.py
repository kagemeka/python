import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class Id():
  self_: bool = False
  author_id: bool = False



@dataclasses.dataclass
class ReferencedTweets():
  id: Id = Id()



@dataclasses.dataclass
class Attachments():
  media_keys: bool = False
  poll_ids: bool = False



@dataclasses.dataclass
class Geo():
  place_id: bool = False



@dataclasses.dataclass
class Expansions():
  author_id: bool = False
  referenced_tweets: (
    ReferencedTweets
  ) = ReferencedTweets()
  in_reply_to_user_id: bool = (
    False
  )
  attachments: Attachments = (
    Attachments()
  )


  NAME = 'expansions'