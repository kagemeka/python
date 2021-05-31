from abc import (
  ABC,
  abstractmethod,
)

from . import (
  Addr,
)

from ..gen import (
  JsonCodec as JC,
  JsonDumpable as JD,
)


from typing import (
  Protocol,
  Optional,
)

from socket import (
  socket,
)

class Hdlr(
  Protocol,
):

  def __call__(
    self,
    *args,
    **kwargs,
  ) -> Optional[JD]:
    return self.handle(
      *args,
      **kwargs,
    )
  

  def handle(
    self,
    data: Optional[
      JD
    ]=None,
    addr: Optional[
      Addr
    ]=None,
    sock: Optional[
      socket
    ]=None,
  ) -> Optional[JD]:
    ...