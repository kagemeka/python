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


  @property
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
    data = data.to_frame().T
    return data
