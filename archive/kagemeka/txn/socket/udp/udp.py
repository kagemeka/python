from .. import (
  BaseTxn,
)

from socket import (
  AF_INET,
  SOCK_DGRAM,
)



class UDP(
  BaseTxn,
):
  def __init__(
    self,
    *args,
    **kwargs,
  ):
    super().__init__(
      family=AF_INET,
      type=SOCK_DGRAM,
      *args,
      **kwargs,
    )
    print('udp')