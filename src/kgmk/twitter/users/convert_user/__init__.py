import dataclasses
import typing
from typing import (
  Optional,
)
from datetime import (
  datetime,
)
from lib import (
  DatetimeFromStr,
)
from .public_metrics import (
  PublicMetrics,
)
from .entities import (
  ConvertEntities,
  Entities,
)



@dataclasses.dataclass
class User():
  id: str
  name: str
  username: str
  created_at: Optional[
    datetime
  ] = None
  protected: Optional[
    bool
  ] = None
  withheld: Optional[
    dict
  ] = None
  location: Optional[
    str
  ] = None
  url: Optional[str] = None
  description: Optional[
    str
  ] = None
  verified: Optional[
    str
  ] = None
  entities: Optional[
    Entities
  ] = None
  profile_image_url: Optional[
    str
  ] = None
  public_metrics: Optional[
    PublicMetrics
  ] = None
  pinned_tweet_id: Optional[
    str
  ] = None



class ConvertUser():
  def __call__(
    self,
    data: dict,
  ) -> User:
    self.__data = data
    self.__convert()
    return self.__user
  

  def __convert(
    self,
  ) -> typing.NoReturn:
    user = User(**self.__data)
    self.__user = user
    self.__public_metrics()
    self.__created_at()
    self.__entities()
  

  def __public_metrics(
    self,
  ) -> typing.NoReturn:
    user = self.__user
    if not user.public_metrics:
      return
    pm = PublicMetrics(
      **user.public_metrics,
    )
    user.public_metrics = pm
  

  def __created_at(
    self,
  ) -> typing.NoReturn:
    user = self.__user
    dt = user.created_at
    if not dt: return
    f = DatetimeFromStr()
    dt = f.rfc3339_format(dt)
    user.created_at = dt
  

  def __entities(
    self,
  ) -> typing.NoReturn:
    user = self.__user
    e = user.entities
    if e is None: return
    f = ConvertEntities()
    user.entities = f(e)