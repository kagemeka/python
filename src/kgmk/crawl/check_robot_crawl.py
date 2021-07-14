import typing
from urllib.robotparser import(
  RobotFileParser,
)



class CheckRobotCrawl():  
  def can_fetch(
    self,
    path: str,
  ) -> bool:
    url = self.__site_url
    return self.__rp.can_fetch(
      useragent='*',
      url=f'{url}/{path}',
    )


  def __init__(
    self,
    site_url: str,
  ) -> typing.NoReturn:
    self.__site_url = site_url
    self.__set_rp()
  

  def __set_rp(
    self,
  ) -> typing.NoReturn:
    url = self.__site_url
    rp = RobotFileParser()
    rp.set_url(
      f'{url}/robot.txt',
    )
    rp.read()
    self.__rp = rp