import typing
from lib.twitter import (
  Request,
)
from . import (
  TweetsParams,
  MentionsParams,
)



class MakeRequest():

  def tweets(
    self,
    id_: str,
    params: TweetsParams,
  ) -> Request:
    api_path = (
      f'/2/users/{id_}/tweets'
    )
    return Request(
      api_path,
      params.to_dict(),
    )


  def mentions(
    self,
    id_: str,
    params: MentionsParams,
  ) -> Request:
    api_path = (
      f'/2/users/{id_}/'
      'mentions'
    )
    return Request(
      api_path,
      params.to_dict(),
    )