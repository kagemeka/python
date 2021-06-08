import typing


class Load():
  def __call__(
    self,
    path: str,
  ) -> typing.Any:
    import json
    with open(
      file=path,
      mode='r',
    ) as fp:
      return json.load(
        fp=fp,
      )