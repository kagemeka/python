import os 
import typing 
from .path import (
  Path,
)


class CurrentFileDir():
  def __call__(
    self,
    __file__: str,
  ) -> str:
    return os.path.abspath(
      Path(__file__).dir,
    )




def jupyter_cfd(
  globals: typing.Callable,
) -> str:
  return globals()['_dh'][0]