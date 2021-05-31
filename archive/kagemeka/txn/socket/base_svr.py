
from multiprocessing import (
  Process,
  Manager,
)

from multiprocessing \
  .managers import (
  Namespace,
)

from typing import (
  NoReturn,
  Tuple,
  Optional,
  Protocol,
)

from abc import (
  abstractmethod,
  ABC,
)


from .. import (
  Addr,  
)

from ...gen import (
  Status,
  JsonDumpable as JD,
  JsonCodec as JC,
  MultiProcessIF,
)

from .. import (
  Hdlr,
  Address,
)




class SvrProto(
  Protocol,
):

  addr: Address



  def bind(
    self,
    address: Address,
  ) -> NoReturn:
    ...


  def prepare(self):
    ...
  

  def close(self):
    ...
  

  def send_(self):
    ...
  

  def receive(self):
    ...

  

  def update_status(self):
    ...
  

  def handle(self):
    ...



from . import (
  BaseTxn,
)  


class BaseSvr(
  MultiProcessIF,
  BaseTxn,
  ABC,
):

  def __init__(
    self,
    hdlr: Hdlr,
    *args,
    **kwargs,
  ):

    super().__init__(
      *args,
      **kwargs,
    )

    self.status = (
      Status.DEACTIVE,
    )

    self.hdlr = hdlr


  @abstractmethod
  def prepare(
    self,
  ):
    self.bind(self.addr)
    ...
    self.activate()


  def create_process(
    self,
  ) -> Process:
    p = Process(
      target=self.run,    
    )
    return p


  def run(
    self,
  ):  
    try:
      self.prepare()
      self.listen_()
    except Exception as e:
      print(e)
      self.close()
    finally:
      self.close()

  
  def listen_(
    self,
  ) -> None:
    while not self.deactive:
      self.update_status()
      if not self.active:
        continue

      self.handle()


  @abstractmethod
  def handle(
    self,
  ) -> NoReturn:
    ... 
    data, addr = self.receive()
    data = self.hdlr(data)
    if data is None:
      return 
    self.send_(
      data,
      addr,
    )
    ...
  

  def update_status(
    self,
  ):
    ns = self.ns
    if not hasattr(
      ns,
      'status',
    ):
      return 

    self.status = ns.status
  

  @property 
  def active(self):
    return (
      self.status 
      == Status.ACTIVE
    )
  

  def activate(self):
    self.status = (
      Status.ACTIVE
    )


  @property
  def deactive(self):
    return (
      self.status
      == Status.DEACTIVE
    )


  def deactivate(self):
    self.status = (
      Status.DEACTIVE
    )
    

  @abstractmethod
  def send_(
    self,
    data: JD,
    *args,
    **kwargs,
  ) -> NoReturn:
    data = JC.encode(data)
    ...


  @abstractmethod
  def receive(
    self,
    *args,
    **kwargs,
  ) -> Tuple[
    JD,
    Optional[Address],
  ]:
    data: bytes
    ...
    data = JC.decode(data)
    return data