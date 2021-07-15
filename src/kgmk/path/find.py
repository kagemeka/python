import typing
from glob import (
  glob,
)
import itertools 


class Find():
  @staticmethod
  def dirs(
    root: str,
  ) -> typing.List[str]:
    dirs = glob(
      f'{root}/**/*/',
      recursive=True,
    )
    return sorted(dirs)
  

  @staticmethod
  def files(
    root: str,
    exts: typing.Iterable[
      str
    ]=('*', ),
  ) -> typing.List[str]:
    files = itertools.chain(*(
      glob(
        f'{root}/**/*.{ext}',
        recursive=True,
      )
      for ext in exts
    ))
    return sorted(files)
