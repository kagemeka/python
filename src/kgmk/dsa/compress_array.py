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
    a = sorted(
      enumerate(a),
      key=lambda x: x[1],
    )
    n = len(a)
    b = [None] * n
    v = [None] * n
    i, mn = -1, -float('inf')
    for j, x in a:
      if x > mn: 
        i += 1
        v[i] = x
        mn = x
      b[j] = i
    self.__v = v
    return b