from multiprocessing \
  .managers import (
  NamespaceProxy,
)

from multiprocessing import (
  Manager,
)



class MultiProcessIF:

  def __init__(
    self,
    ns: NamespaceProxy=None,
    *args,
    **kwargs,
  ):
    if ns is None:
      manager = Manager()
      ns = manager.Namespace()
      
    self.ns = ns
    super().__init__(
      *args,
      **kwargs,
    )