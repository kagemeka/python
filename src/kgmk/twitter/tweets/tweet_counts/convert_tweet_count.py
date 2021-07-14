import dataclasses
from datetime import (
  datetime,
)
import typing
from lib import (
  DatetimeFromStr,
)



@dataclasses.dataclass
class TweetCount():
  start: datetime
  end: datetime
  tweet_count: int



class ConvertTweetCount():
  def __call__(
    self,
    data: dict,
  ) -> TweetCount:
    self.__data = data
    self.__convert()
    return self.__cnt
  

  def __convert(
    self,
  ) -> typing.NoReturn:
    self.__cnt = TweetCount(
      **self.__data,
    )
    self.__start()
    self.__end()
  

  def __start(
    self,
  ) -> typing.NoReturn:
    f = DatetimeFromStr()
    cnt = self.__cnt
    s  = f.rfc3339_format(
      cnt.start,
    )
    cnt.start = s


  def __end(
    self,
  ) -> typing.NoReturn:
    f = DatetimeFromStr()
    cnt = self.__cnt
    cnt.end = f.rfc3339_format(
      cnt.end,
    )