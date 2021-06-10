from typing import (
  NoReturn,
  Optional,
)

from ....gen import (
  JsonDumpable as JD,
  JsonCodec as JC,
)

from . import (
  TCP,
)



class TCPClient(
  TCP,
):

  def connect_(
    self,
  ) -> NoReturn:
    self.connect(
      self.addr,
    )


  def send_(
    self,
    data: JD,
  ) -> NoReturn:
    data = JC.encode(data)
    self.sendall(data)

    
  def receive(
    self,
  ) -> JD:
    chunks = [] 
    while True:
      chunk = self.recv(
        self.bufsize,
      )
      if not chunk:
        break
      chunks.append(chunk)
    data = b''.join(chunks)
    data = JC.decode(data)
    return data