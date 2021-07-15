import dataclasses
import typing
from typing import (
  Optional,
)



@dataclasses.dataclass
class TweetFields():
  id: bool = True
  text: bool = True
  attachments: bool = False
  author_id: bool = False
  context_annotations: bool = (
    False
  )
  conversation_id: bool = False
  created_at: bool = False
  entities: bool = False
  geo: bool = False
  in_reply_to_user_id: bool = (
    False
  )
  lang: bool = False
  non_public_metrics: bool = (
    False
  )
  organic_metrics: bool = False
  possibly_sensitive: bool = (
    False
  )
  promoted_metrics: bool = (
    False
  )
  public_metrics: bool = False
  referenced_tweets: bool = (
    False
  )
  reply_settings: bool = False
  source: bool = False
  withheld: bool = False


  NAME = 'tweet.fields'