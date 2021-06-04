from . import (
  UDP,
)

from ....gen import (
  JsonCodec as JC,
  JsonDumpable as JD,
  MultiProcessIF,
)

from .. import (
  BaseSvr,
)

from typing import (
  Tuple,
  NoReturn,
  Optional,
)

from ... import (
  Address,
  Addr,
  Hdlr,
)

from multiprocessing \
  .managers import (
  NamespaceProxy,
)



class UDPSvr(
  UDP,
  BaseSvr,
):

  def __init__(
    self,
    addr: Addr,
    hdlr: Hdlr,
    ns: NamespaceProxy,
    *args,
    **kwargs,
  ):

    super().__init__(
      addr=addr,
      hdlr=hdlr,
      ns=ns,
      *args,
      **kwargs,
    )
    

  def prepare(self):
    self.bind(self.addr)
    self.activate()


  def handle(
    self, 
  ) -> NoReturn:
    data, addr = self.receive()
    data = self.hdlr(
      data=data,
      addr=addr,
    )
    if data is None:
      return
    self.send_(
      data=data,
      addr=addr,
    )


  def receive(
    self,
  ) -> Tuple[
    JD,
    Optional[Address],
  ]:

    data, addr = self.recvfrom(
      self.bufsize,
    )
    data = JC.decode(data)
    return data, addr


  def send_(
    self,
    data: JD,
    addr: Address,
  ) -> NoReturn:
    data = JC.encode(data)
    self.sendto(
      data,
      addr,
    )