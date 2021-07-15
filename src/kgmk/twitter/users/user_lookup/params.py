import dataclasses
from dataclasses import (
  field,
)
import typing
from typing import (
  Optional,
)
from .. import (
  Expansions,
)
from ...fields import (
  TweetFields,
  UserFields,
)
from ... import (
  ConvertParams,
)



@dataclasses.dataclass
class Params():
  expansions: Expansions = (
    Expansions()
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
    convert = ConvertParams()
    params = (
      self.expansions,
      self.tweet_fields,
      self.user_fields,
    )
    return {
      p.name: p.string
      for p in map(
        convert,
        params,
      )
    }



@dataclasses.dataclass
class ByIdParams(
  Params,
):
  ...



@dataclasses.dataclass
class ByIdsParams(
  Params,
):
  ids: typing.List[
    str
  ] = field(
    default_factory=list,
  )


  def to_dict(
    self,
  ) -> dict:
    ids = ','.join(self.ids)
    return {
      'ids': ids,
      **super().to_dict(),
    }



@dataclasses.dataclass
class ByUsernameParams(
  Params,
):
  ...



@dataclasses.dataclass
class ByUsernamesParams(
  Params,
):
  usernames: typing.List[
    str
  ] = field(
    default_factory=list,
  )


  def to_dict(
    self,
  ) -> dict:
    usernames = ','.join(
      self.usernames,
    )
    return {
      'usernames': usernames,
      **super().to_dict(),
    }