from datetime import (
  datetime, 
  timezone, 
  timedelta,
)


from .. import (
  DataClass,
)

from dataclasses import (
  dataclass,
)


from typing import (
  Final,
  final,
)


@dataclass
class DTM(
  DataClass,
):
  delta_from_utc: int


  @property 
  def td(
    self,
  ) -> timedelta:
    d = self.delta_from_utc
    td = timedelta(hours=d) 
    return td 
  

  @property 
  def tz(
    self,
  ) -> timezone:
    tz = timezone(
      self.td,
    )
    return tz 
  

  @property 
  def now(
    self,
  ) -> datetime:
    dt = datetime.now(
      self.tz, 
    )
    return dt
  

  def __repr__(
    self,
  ) -> str:
    return self.compressed

  

  @property
  def compressed(
    self,
  ) -> str:
    fmt = r'%Y%m%d%H%M%S'
    s = self.now.strftime(
      format=fmt,
    )
    return s
  
  
  @property 
  def iso(
    self,
  ) -> str:
    s = self.now.isoformat()
    return s 



@final
@dataclass 
class DTMs(
  DataClass,
):
  JP: Final[DTM] = DTM(
    delta_from_utc=+9,
  )