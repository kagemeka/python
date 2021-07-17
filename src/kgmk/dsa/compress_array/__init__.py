import typing 



class CompressArray():
  def retrieve(
    self,
    i: int,
  ) -> int:
    return self.__v[i]
  

  def __call__(
    self,
    a: typing.Iterable[int],
  ) -> typing.List[int]:
    from bisect import (
      bisect_left as f,
    )
    v = sorted(set(a))
    self.__v = v
    return [f(v, x) for x in a]