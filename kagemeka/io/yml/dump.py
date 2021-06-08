import typing

class Dump():
  def __call__(
    self,
    data: object,
    path: str,
  ) -> typing.NoReturn:
    with open(
      file=path,
      mode='w',
    ) as stream:
      yaml.dump(
        data=data,
        stream=stream,
      )
    
      