from enum import (
  Enum,
  auto,
  unique,
)


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



@unique
class FourCC(Enum):
  MP4V = auto()
  XVID = auto()


@dataclass
class VideoFormat(
  BaseFormat,
):
  fourcc: FourCC


@dataclass
class VideoFormats(
  BaseFormats,
):
  mp4: VideoFormat = (
    VideoFormat(
      name=FF.MP4,
      fourcc=FourCC.MP4V,
    )
  )

  avi: VideoFormat = (
    VideoFormat(
      name=FF.AVI,
      fourcc=FourCC.XVID,
    )
  )

  mov: VideoFormat = (
    VideoFormat(
      name=FF.MOV,
      fourcc=FourCC.MP4V,
    )
  )


  @classmethod 
  def get_fmt(
    cls,
    path: Path_,
  ) -> VideoFormat:
    fmt = super().get_fmt(path)
    return fmt