from typing import (
  List,
  Protocol,
  Union,
)
from pathlib import Path
import json


import io 



class Readable(
  Protocol,
):

  def read(
    self
  ) -> bytes:
    ...
  

  def readline(
    self,
  ) -> bytes:
    ...
  

  def readlines(
    self,
  ) -> List[bytes]:
    ...



Input = Union[
  io.TextIOWrapper,
  io.BufferedReader,
  Readable,
  str,
  bytes,
  int,
]


Path_ = Union[Path, str]


JsonDumpable = Union[
  str, 
  int,
  float,
  list,
  tuple,
  dict,
  bool, 
  None,
]