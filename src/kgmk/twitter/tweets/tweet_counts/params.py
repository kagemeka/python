import dataclasses
from dataclasses import (
  fields,
)
import typing
from typing import (
  Optional,
)
from datetime import (
  datetime,
)

from lib import (
  DatetimeToRFC3339,
)



@dataclasses.dataclass
class Params():
  query: str
  end_time: Optional[
    datetime
  ] = None
  granularity: Optional[
    str
  ] = None
  since_id: Optional[
    str
  ] = None
  start_time: Optional[
    datetime
  ] = None
  until_id: Optional[
    str
  ] = None


  def to_dict(
    self,
  ) -> dict:
    params = {}
    fn = DatetimeToRFC3339()
    for f in fields(self):
      f = f.name
      v = getattr(self, f)
      if v is None: continue
      t = type(v)
      if t == int or t == str:
        params[f] = v
        continue
      if t == datetime:
        params[f] = fn(v)
        continue
    return params