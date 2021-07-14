import typing


class ManageId():
  def __call__(
    self,
    *args,
    **kwargs,
  ) -> int:
    return self.get_id(
      *args,
      **kwargs,
    )


  def __getitem__(
    self,
    *args,
    **kwargs,
  ) -> typing.Hashable:
    return self.retrieve(
      *args,
      **kwargs,
    )


  def __init__(
    self,
    maxsize: int=1 << 16,
  ) -> typing.NoReturn:
    self.__values = (
      [None] * maxsize
    )
    self.__cache = dict()

  
  def get_id(
    self, 
    value: typing.Hashable,
  ) -> int:
    cache = self.__cache
    id_ = cache.get(
      value,
      len(cache),
    )
    cache[value] = id_
    self.__values[id_] = value
    return id_


  def retrieve(
    self,
    id_: int,
  ) -> typing.Hashable:
    return self.__values[id_]