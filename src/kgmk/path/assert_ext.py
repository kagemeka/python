import re 
import typing
from .path import (
  Path,
)


class AssertExt():
  def __call__(
    self,
    path: str,
    ext: str=r'.+',
  ) -> bool:
    ptn = re.compile(
      ext,
      re.IGNORECASE,
    )
    return ptn.match(
      Path(path).ext,
    ) is not None