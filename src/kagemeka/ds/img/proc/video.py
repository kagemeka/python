from __future__ import (
  annotations,
)

from dataclasses import (
  dataclass,
)

from . import (
  ImgProc as IP,
  VideoProps as VProp,
  FrameSz,
  ChangeProps,
)

from ....gen import (
  PathManager as PM,
  DataClass,
)

import cv2
import os 

from typing import (
  Optional,
  NoReturn,
  final,
)

import numpy as np


@final
@dataclass
class Video(
  DataClass,
):
  src: Optional[str] = None 
  dst: Optional[str] = None
  src_props: Optional[
    VProp
  ]=None
  dst_props: Optional[
    VProp
  ]=None
  cap: Optional[
    cv2.VideoCapture
  ] = None 
  writer: Optional[
    cv2.VideoWriter
  ] = None


  @classmethod 
  def make(
    cls,
    src: str,
    dst: Optional[str]=None,
    chprops: Optional[
      ChangeProps
    ]=None,
  ) -> Video:
    from . import (
      VideoProc as VProc,
    )
    cap = cv2.VideoCapture(
      src,
    )
    src_props = VProp.from_cap(
      cap=cap,
    )
    vid = cls(
      src_props=src_props,
      src=src,
      dst=dst,
      cap=cap,
    )
    if dst is None:
      return vid 

    dst_props = src_props  
    if chprops is not None:
      dst_props = chprops(
        dst_props,
      )
    vid.dst_props = dst_props

    writer = VProc.make_writer(
      vid,
    )
    vid.writer = writer 
    return vid
  

  @property
  def name(
    self,
  ) -> str:
    return PM.root(
      self.base,
    )


  @property
  def base(
    self,
  ) -> str:
    return PM.base(
      self.src,
    )


  @property
  def is_open(
    self,
  ) -> bool:
    return self.cap.isOpened()
  

  def read(
    self,
    resize: bool=True,
  ) -> Optional[
    np.ndarray
  ]:
    (
      success,
      frame,
    ) = self.cap.read()
    if not success:
      return None
    if not resize:
      return frame 
    prop = self.dst_props
    if prop is None:
      return frame
    size = prop.size 
    if size is None:
      return frame 
    frame = IP.resize_img(
      img=frame,
      tgt=size,
    )
    return frame


  def write(
    self, 
    frame: np.ndarray,
  ) -> NoReturn:
    size = self.dst_props.size
    frame = IP.resize_img(
      img=frame,
      tgt=size,
    )
    self.writer.write(frame)

  
  def release(
    self,
  ) -> NoReturn:
    for x in (
      self.cap,
      self.writer,
    ):
      if x is None:
        continue
      x.release()


  def __enter__(
    self,
  ) -> Video:
    return self 
  

  def __exit__(
    self,
    exc_type,
    exc_value,
    traceback,
  ) -> NoReturn:
    self.release()
