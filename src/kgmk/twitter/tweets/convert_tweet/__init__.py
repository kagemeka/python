import dataclasses
import typing
from typing import (
  Optional,
  List,
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
from .context_annotation \
import (
  ConvertContextAnnotation,
  ContextAnnotation,
)
from .referenced_tweet import (
  ReferencedTweet,
)
from .attachments import (
  Attachments,
)
from .geo import (
  ConvertGeo,
  Geo,
)
from .withheld import (
  Withheld,
)
from .non_public_metrics \
import (
  NonPublicMetrics,
)
from .organic_metrics import (
  OrganicMetrics,
)
from .promoted_metrics import (
  PromotedMetrics,
)



@dataclasses.dataclass
class Tweet():
  id: str
  text: str
  attachments: Optional[
    Attachments
  ] = None
  author_id: Optional[
    str
  ] = None
  context_annotations: (
    Optional[List[
      ContextAnnotation
    ]]
  ) = None
  conversation_id: Optional[
    str
  ] = None
  created_at: Optional[
    datetime
  ] = None
  entities: Optional[
    Entities
  ] = None
  geo: Optional[Geo] = None 
  in_reply_to_user_id: (
    Optional[str]
  ) = None
  lang: Optional[str] = None
  possibly_sensitive: Optional[
    bool
  ] = None
  public_metrics: Optional[
    PublicMetrics
  ] = None
  non_public_metrics: Optional[
    NonPublicMetrics
  ] = None
  organic_metrics: Optional[
    OrganicMetrics
  ] = None
  promoted_metrics: Optional[
    PromotedMetrics
  ] = None
  referenced_tweets: Optional[
    List[ReferencedTweet]
  ] = None
  reply_settings: Optional[
    str
  ] = None
  source: Optional[str] = None
  withheld: Optional[
    Withheld
  ] = None



class ConvertTweet():
  def __call__(
    self,
    data: dict,
  ) -> Tweet:
    self.__data = data
    self.__convert()
    return self.__tweet
  

  def __convert(
    self,
  ) -> typing.NoReturn:
    tweet = Tweet(
      **self.__data,
    )
    self.__tweet = tweet
    self.__public_metrics()
    self.__entities()
    self.__context_annotations()
    self.__referenced_tweets()
    self.__attachments()
    self.__created_at()
    self.__geo()
    self.__withheld()
    self.__non_public_metrics()
    self.__organic_metrics()
    self.__promoted_metrics()
  

  def __public_metrics(
    self,
  ) -> typing.NoReturn:
    tweet = self.__tweet
    pm = tweet.public_metrics
    if pm is None: return
    pm = PublicMetrics(**pm)
    tweet.public_metrics = pm
  

  def __entities(
    self,
  ) -> typing.NoReturn:
    tweet = self.__tweet
    ent = tweet.entities
    if ent is None: return
    f = ConvertEntities()
    tweet.entities = f(ent)
  

  def __context_annotations(
    self,
  ) -> typing.NoReturn:
    tw = self.__tweet
    ls = tw.context_annotations
    if ls is None: return
    f = ConvertContextAnnotation()
    tw.context_annotations = [
      f(annot)
      for annot in ls
    ]


  def __referenced_tweets(
    self,
  ) -> typing.NoReturn:
    tw = self.__tweet
    ls = tw.referenced_tweets
    if ls is None: return
    tw.referenced_tweets = [
      ReferencedTweet(**x)
      for x in ls
    ]
  

  def __attachments(
    self,
  ) -> typing.NoReturn:
    tw = self.__tweet
    x = tw.attachments
    if x is None: return
    x = Attachments(**x)
    tw.attachments = x
  

  def __created_at(
    self,
  ) -> typing.NoReturn:
    tw = self.__tweet
    x = tw.created_at
    if x is None: return
    f = DatetimeFromStr()
    x = f.rfc3339_format(x)
    tw.created_at = x
  

  def __geo(
    self,
  ) -> typing.NoReturn:
    tw = self.__tweet
    x = tw.geo
    if x is None: return
    f = ConvertGeo()
    tw.geo = f(x)
  

  def __withheld(
    self,
  ) -> typing.NoReturn:
    tw = self.__tweet
    x = tw.withheld
    if x is None: return
    tw.withled = Withheld(**x)
  

  def __non_public_metrics(
    self,
  ) -> typing.NoReturn:
    tw = self.__tweet
    x = tw.non_public_metrics
    if x is None: return 
    x = NonPublicMetrics(**x)
    tw.non_public_metrics = x

  
  def __organic_metrics(
    self,
  ) -> typing.NoReturn:
    tw = self.__tweet
    x = tw.organic_metrics
    if x is None: return 
    x = OrganicMetrics(**x)
    tw.organic_metrics = x
  

  def __promoted_metrics(
    self,
  ) -> typing.NoReturn:
    tw = self.__tweet
    x = tw.promoted_metrics
    if x is None: return
    x = PromotedMetrics(**x)
    tw.promoted_metrics = x