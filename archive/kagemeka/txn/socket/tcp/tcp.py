from .. import (
  BaseTxn,
)

from socket import (
  AF_INET,
  SOCK_STREAM,
)



class TCP(
  BaseTxn,
):
  def __init__(
    self,
    *args,
    **kwargs,
  ):
    super().__init__(
      family=AF_INET,
      type=SOCK_STREAM,
      *args,
      **kwargs,
    )
    print('tcp')
