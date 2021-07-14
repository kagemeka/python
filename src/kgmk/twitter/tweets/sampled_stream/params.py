import typing
import dataclasses
from typing import (
  Optional,
)
from dataclasses import (
  fields,
)
from ...fields import (
  TweetFields,
  PollFields,
  MediaFields,
  PlaceFields,
  UserFields,
)
from ... import (
  ConvertParams,
)
from .. import (
  Expansions,
)



@dataclasses.dataclass 
class Params():
  backfill_minutes: Optional[
    int
  ] = None
  media_fields: MediaFields = (
    MediaFields()
  )
  place_fields: PlaceFields = (
    PlaceFields()
  )
  poll_fields: PollFields = (
    PollFields()
  )
  tweet_fields: TweetFields = (
    TweetFields()
  )
  user_fields: UserFields = (
    UserFields()
  )


  def to_dict(
    self,
  ) -> dict:
    fn = ConvertParams()
    ls = (
      self.media_fields,
      self.place_fields,
      self.poll_fields,
      self.tweet_fields,
      self.user_fields,
    )
    params = {
      p.name: p.string
      for p in map(fn, ls)
    }
    for f in fields(self):
      f = f.name
      v = getattr(self, f)
      if v is None: continue
      t = type(v)
      if t == str:
        params[f] = v
        continue
    return params