import typing



class ReadStdin:
  def __call__(
    self,
  ) -> bytes:
    return next(self.__chunks)
    

  def __init__(
    self,
  ) -> typing.NoReturn:
    import sys
    self.__buf = (
      sys.stdin.buffer
    )
    self.__chunks = (
      self.__read_chunks()
    )


  def int(
    self,
  ) -> int:
    return int(self())


  def __read_chunks(
    self,
  ) -> typing.Iterator[bytes]:
    while 1:
      l = self.__buf.readline()
      for chunk in l.split():
        yield chunk
  

  def str(
    self,
  ) -> str:
    b = self()
    return b.decode()