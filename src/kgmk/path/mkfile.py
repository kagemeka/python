import typing
from .prepare_dir import (
  PrepareDir,
)

 
class Mkfile():
  def __call__(
    self,
    path: str,
  ) -> typing.NoReturn:
    PrepareDir()(path)
    with open(
      file=path,
      mode='w',
    ) as _:
      pass 
