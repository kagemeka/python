import socket 

from .. import (
  Addr,
)

from ...gen import (
  Status,
  JsonCodec as JC,
)

import json 


class BaseTxn(
  socket.socket,
):
  def __init__(
    self, 
    addr: Addr,
    bufsize: int=1 << 10,
    *args,
    **kwargs,
  ):
    super().__init__(
      *args,
      **kwargs,
    )

    self.addr = (
      *addr,
    )

    self.bufsize = bufsize