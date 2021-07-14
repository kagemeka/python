from dataclasses import (
  dataclass,
)

from abc import (
  ABC,
  abstractclassmethod,
)

from .... import (
  DataClass,
  FileFormat as FF,
)

from .. import (
  Path_,
)


@dataclass
class BaseFormat(
  DataClass,
  ABC,
):
  name: FF


@dataclass
class BaseFormats(
  DataClass,
  ABC,
):

  @classmethod
  def assert_fmt(
    cls,
    path: Path_,
  ) -> bool:
    from ... import (
      PathManager as PM,
    )
    ext = PM.ext(path)
    ok = (
      ext in cls()
    )
    return ok
  

  @abstractclassmethod
  def get_fmt(
    cls,
    path: Path_,
  ) -> BaseFormat: 
    from ... import (
      PathManager as PM,
    )
    ok = cls.assert_fmt(path)
    if not ok:
      return 

    ext = PM.ext(path)
    fmt = getattr(cls(), ext)
    return fmt