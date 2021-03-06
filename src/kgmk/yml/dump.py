import typing


class Dump():
  def __call__(
    self,
    data: typing.Any,
    path: str,
  ) -> typing.NoReturn:
    import yaml
    with open(
      file=path,
      mode='w',
    ) as stream:
      yaml.dump(
        data=data,
        stream=stream,
      )