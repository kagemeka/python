import requests 
import typing 



class SendRequest():
  def __call__(
    self,
    params: dict,
  ) -> (
    requests.models.Response
  ):
    return requests.get(
      url=self.__url,
      params=params,
    )
  

  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__url = (
      'http://'
      'api.jstage.jst.go.jp/'
      'searchapi/do'
    )
