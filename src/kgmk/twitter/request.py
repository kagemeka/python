import dataclasses
import requests
import typing
from .auth import (
  TwitterAuth,
)


@dataclasses.dataclass
class Request():
  api_path: str
  params: dict



class SendRequest():
  def __call__(
    self,
    request: Request,
  ) -> (
    requests.models.Response
  ):
    url = self.__base_url
    path = request.api_path
    url = f'{url}{path}'
    response = requests.get(
      url=url,
      headers=self.__headers,
      params=request.params,
    )
    return response
  

  def __init__(
    self,
    auth: TwitterAuth,
  ) -> typing.NoReturn:
    token = (
      'Bearer '
      f'{auth.bearer_token}'
    )
    self.__headers = {
      'Authorization': token,
    }
    self.__base_url = (
      'https://api.twitter.com'
    )