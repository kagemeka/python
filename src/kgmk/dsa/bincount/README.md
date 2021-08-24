import typing


class BinCount():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    c = [0] * (max(a) + 1)
    for x in a: c[x] += 1
    return c
