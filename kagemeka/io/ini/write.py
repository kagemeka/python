import typing 
from typing import (
  Any,
  Mapping,
)


class Write():
  def __call__(
    self,
    data: Mapping[
      str,
      Mapping[str, Any],
    ],
    path: str,
  ) -> typing.NoReturn:
    from configparser import (
      ConfigParser,
    )
    cp = ConfigParser()
    cp.read_dict(data)
    with open(
      file=path,
      mode='w',
    ) as f:
      cp.write(f)