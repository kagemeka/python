import typing
from . import (
  Params,
)
from ... import (
  Request,
)


class MakeRequest():
  def __call__(
    self,
    params: Params,
  ) -> Request:
    api_path = (
      '/2/tweets/sample/'
      'stream'
    )
    return Request(
      api_path,
      params.to_dict(),
    ) 