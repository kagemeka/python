import dataclasses
from dataclasses import (
  fields,
)
import typing
from typing import (
  Optional,
)
from datetime import (
  datetime,
)
from .. import (
  Expansions,
)
from ...fields import (
  TweetFields,
  UserFields,
  MediaFields,
  PlaceFields,
  PollFields,
)
from ... import (
  ConvertParams,
)

from lib import (
  DatetimeToRFC3339,
)




@dataclasses.dataclass
class Params():
  end_time: Optional[
    datetime
  ] = None
  expansions: Expansions = (
    Expansions()
  )
  max_results: Optional[
    int
  ] = None
  media_fields: MediaFields = (
    MediaFields()
  )
  pagination_token: Optional[
    str
  ] = None
  place_fields: PlaceFields = (
    PlaceFields()
  )
  poll_fields: PollFields = (
    PollFields()
  )
  since_id: Optional[
    str
  ] = None
  start_time: Optional[
    datetime
  ] = None
  tweet_fields: TweetFields = (
    TweetFields()
  )
  until_id: Optional[
    str
  ] = None
  user_fields: UserFields = (
    UserFields()
  )
    

  def to_dict(
    self,
  ) -> dict:
    fn = ConvertParams()
    ls = (
      self.expansions,
      self.tweet_fields,
      self.user_fields,
      self.media_fields,
      self.poll_fields,
      self.place_fields,
    )
    params = {
      p.name: p.string
      for p in map(fn, ls)
    }
    fn = DatetimeToRFC3339()
    for f in fields(self):
      f = f.name
      v = getattr(self, f)
      if v is None: continue
      t = type(v)
      if t == int or t == str:
        params[f] = v
        continue
      if t == datetime:
        params[f] = fn(v)
        continue
    return params



@dataclasses.dataclass
class Exclude():
  retweets: bool = False
  replies: bool = False

  NAME = 'exclude'



@dataclasses.dataclass
class TweetsParams(
  Params,
):
  exclude: Exclude = Exclude()


  def to_dict(
    self,
  ) -> dict:
    fn = ConvertParams()
    p = fn(self.exclude)
    return {
      p.name: p.string,
      **super().to_dict(), 
    }



@dataclasses.dataclass
class MentionsParams(
  Params,
):
  ...