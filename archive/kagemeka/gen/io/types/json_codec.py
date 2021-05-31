import json 

from typing import (
  Any,
)

from . import (
  JsonDumpable,
)



class JsonCodec:

  
  @staticmethod 
  def encode(
    obj: JsonDumpable,
  ) -> bytes:
    return json.dumps(
      obj,
    ).encode()
  

  @staticmethod 
  def decode(
    obj: bytes,
  ) -> JsonDumpable:
    return json.loads(
      obj.decode(),
    )