from typing import Union 
from pathlib import Path
import json


Path_ = Union[Path, str]


class JsonCodec:
  @staticmethod 
  def encode(obj):
    return json.dumps(
      obj,
    ).encode()
  

  @staticmethod 
  def decode(obj):
    return json.loads(
      obj.decode(),
    )



from typing import (
  List,
  Union,
)


import io 


Input = Union[
  io.TextIOWrapper,
  io.BufferedReader,
  str,
  bytes,
  int,
]