import os
import typing
from .path import (
  Path,
)


class PrepareDir():
  def __call__(
    self,
    path: str,
  ) -> typing.NoReturn:
    os.makedirs(
      name=Path(path).dir,
      exist_ok=True,
    )