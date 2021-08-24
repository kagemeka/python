import typing


class FlatNonzero():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    return [i for i, x in enumerate(a) if x]