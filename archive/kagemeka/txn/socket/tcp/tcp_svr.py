from . import (
  TCP,
)

from socket import (
  socket,
  timeout,
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



class TCPSvr(
  TCP,
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
    self.listen(1 << 0)
    self.activate()


  def handle(
    self, 
  ) -> NoReturn:
    conn, addr = self.accept()
    with conn:
      conn.settimeout(1e-1)
      data = self.receive(
        conn,
      )
      data = self.hdlr(
        data=data,
        addr=addr,
        sock=conn,
      )
      if data is None:
        return
      self.send_(
        data=data,
        conn=conn,
      )


  def receive(
    self,
    conn: socket,
  ) -> JD:
    chunks = []
    while True:
      try:
        chunk = conn.recv(
          self.bufsize,
        )
      except timeout:
        break
      except:
        continue
      if not chunk:
        break 
      chunks.append(chunk)
    data = b''.join(chunks)
    data = JC.decode(data)
    return data

  
  def send_(
    self,
    data: JD,
    conn: socket,
  ) -> NoReturn:
    data = JC.encode(data)
    conn.sendall(data)
