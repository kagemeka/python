import typing 



class CompressArray():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.NoReturn:
    from bisect import bisect_left 
    v = sorted(set(a))
    self.__v = v 
    return [bisect_left(v, x) for x in a]


  def __getitem__(
    self,
    i: int,
  ) -> int:
    return self.retrieve(i)


  def retrieve(
    self,
    i: int,
  ) -> int:
    return self.__v[i]