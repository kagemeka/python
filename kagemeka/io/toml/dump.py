from typing import (
  Mapping,
  Any,
)

class Dump():
  def __call__(
    self,
    data: Mapping[str, Any],
    path: str,
  ) -> typing.NoReturn:
    import toml
    with open(
      file=path,
      mode='w',
    ) as f:
      toml.dump(
        o=data,
        f=f,
      )