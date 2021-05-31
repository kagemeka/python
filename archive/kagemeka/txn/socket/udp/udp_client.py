from . import (
  UDP,
)

from ... import (
  Address,
)

from ....gen import (
  JsonCodec as JC,
  JsonDumpable as JD,
)

from typing import (
  Optional,
  NoReturn,
  Tuple,
)


class UDPClient(UDP):


  def send_(
    self,
    data: JD,
  ) -> NoReturn:
    data = JC.encode(data)
    self.sendto(
      data,
      self.addr,
    )

    
  def receive(
    self,
  ) -> JD:
    data = self.recv(
      self.bufsize,
    )
    data = JC.decode(data)
    return data