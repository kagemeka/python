import typing


class Dump():
  def __call__(
    self,
    data: typing.Any,
    path: str,
  ) -> typing.NoReturn:
    import json 
    with open(
      file=path,
      mode='w',
    ) as fp:
      json.dump(
        obj=data,
        fp=fp,
      )
