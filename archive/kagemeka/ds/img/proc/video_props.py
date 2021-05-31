from __future__ import (
  annotations,
)

from dataclasses import (
  dataclass,
)

from typing import (
  final,
  Optional,
  Callable,
)

from ....gen import (
  DataClass,
)

import cv2 

from . import (
  FrameSz,
)


@final
@dataclass
class VideoProps(
  DataClass,
):
  frame_cnt: Optional[
    int
  ] = None
  fps: Optional[
    float
  ] = None
  size: Optional[
    FrameSz
  ] = None
  
  
  @classmethod 
  def from_cap(
    cls,
    cap: cv2.VideoCapture,
  ) -> VideoProps:
    frame_cnt = int(cap.get(
      cv2.CAP_PROP_FRAME_COUNT,
    ))
    fps: float = cap.get(
      cv2.CAP_PROP_FPS,
    )
    h = int(cap.get(
      cv2
      .CAP_PROP_FRAME_HEIGHT,
    ))
    w = int(cap.get(
      cv2.CAP_PROP_FRAME_WIDTH,
    ))
    size = FrameSz(
      width=w,
      height=h,
    )
    prop = cls(
      frame_cnt=frame_cnt,
      fps=fps,
      size=size,
    )
    return prop 



ChangeProps = Callable[
  [VideoProps],
  VideoProps,
]