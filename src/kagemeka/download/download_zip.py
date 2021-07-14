import dataclasses
import io 
import requests 
import typing
from typing import (
  NoReturn,
)
import zipfile


@dataclasses.dataclass
class Cfg():
  path: str
  url: str


class DownloadZip():
  r'''
  
  download zip and extract it

  '''
  
  def __call__(
    self,
  ) -> NoReturn:
    self.__url_fetch()
    self.__zip()
    self.__extract()
    

  def __extract(
    self,
  ) -> NoReturn:
    self.__zip_file.extractall(
      path=self.__cfg.path,
    )


  def __init__(
    self,
    cfg: Cfg,
  ) -> NoReturn:
    self.__cfg = cfg


  def __url_fetch(
    self,
  ) -> NoReturn:
    self.__req = requests.get(
      url=self.__cfg.url,
      stream=True,
    )
  

  def __zip(
    self,
  ) -> NoReturn:
    req = self.__req
    zip_file = zipfile.ZipFile(
      io.BytesIO(req.content),
    )
    self.__zip_file = zip_file