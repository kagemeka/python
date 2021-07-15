import typing
from kgmk.twitter import (
  Request,
)
from . import (
  Params,
)



class MakeRequest():
  def __call__(
    self,
    params: Params,
  ) -> Request:
    api_path = (
      '/2/tweets/counts/recent'
    )
    return Request(
      api_path,
      params.to_dict(),
    )