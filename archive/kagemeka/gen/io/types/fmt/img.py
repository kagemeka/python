from dataclasses import (
  dataclass,
)

from . import (
  BaseFormats,
  BaseFormat,
)

from .... import (
  FileFormat as FF,
)

from .. import (
  Path_,
)


@dataclass 
class ImgFormat(
  BaseFormat,
):
  ...


@dataclass 
class ImgFormats(
  BaseFormats,
):
  png: ImgFormat = (
    ImgFormat(
      name=FF.PNG,
    )
  )

  jpg: ImgFormat = (
    ImgFormat(
      name=FF.JPG,
    )
  )

  jpeg: ImgFormat = (
    ImgFormat(
      name=FF.JPEG,
    )
  )

  @classmethod 
  def get_fmt(
    cls,
    path: Path_,
  ) -> ImgFormat:
    fmt = super().get_fmt(path)
    return fmt