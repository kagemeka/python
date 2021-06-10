from typing import (
  List,
  Hashable,
)

from dataclasses import (
  dataclass,
)


class IDManager(
  dict,
):


  def __init__(
    self,
    maxsize: int=1 << 18,
  ):
    super().__init__()
    self.values = (
      [None] * maxsize
    )

  
  def retrieve(
    self,
    id_: int,
  ):
    return self.values[id_]

  
  def get_id(
    self, 
    value: Hashable,
  ):
    id_ = self.get(
      value,
      len(self),
    )
    self[value] = id_
    self.values[id_] = value
    return id_
  

  def __call__(
    self,
    *args,
    **kwargs,
  ):
    return self.get_id(
      *args,
      **kwargs,
    )


  def __getitem__(
    self,
    *args,
    **kwargs,
  ):
    return self(
      *args,
      **kwargs,
    )