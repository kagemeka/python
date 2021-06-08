from __future__ import (
  annotations,
)
from dataclasses import (
  dataclass,
  astuple,
  asdict,
  field,
  fields
)

from abc import (
  ABC,
)
import pandas as pd



@dataclass 
class DataClass(ABC):


  @property
  def values(self):
    return astuple(self)


  def __iter__(self):
    return iter(self.values)


  def dic(self):
    return asdict(self)


  @property
  def fields(self):
    return fields(self)
  

  @property
  def keys(self):
    res = tuple(
      f.name
      for f in self.fields
    )
    return res

  
  @classmethod 
  def from_dict(
    cls,
    dic,
  ):
    return cls(**dic)

  @classmethod
  def from_yml(
    cls,
    path: str,
  ) -> cls:
    from kagemeka.io import (
      yml,
    )
    load = yml.Load()
    return cls(**load(path))
  

  def __contains__(
    self,
    item: str,
  ) -> bool:
    return hasattr(
      self, 
      item,
    )
  

  def __getitem__(
    self,
    item: str,
  ):
    return getattr(
      self,
      item,
    )


  def dataframe(
    self,
  ) -> pd.DataFrame:
    data = self.dic()
    data = pd.Series(data)
    return data.to_frame().T

