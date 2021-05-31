from ....gen import (
  PathManager as PM,
  Path_,
)

import cv2
import numpy as np 

from typing import (
  Set, 
  Union,
  List,
  Tuple,
  Iterable,
  Optional,
  NoReturn,
)

import pathlib 
import pandas as pd 
import os 


from dataclasses import (
  dataclass,
  asdict,
  astuple,
)


from . import (
  FrameSz,
)


class ImgProc:
  
  @staticmethod 
  def scale_ratio(
    src: FrameSz,
    tgt: FrameSz,
  ) -> float:
    w0, h0 = *src,
    w1, h1 = *tgt,
    r = min(
      w1 / w0,
      h1 / h0,
    )
    return r


  @classmethod 
  def resize_box(
    cls,
    src: FrameSz,
    tgt: FrameSz,
  ) -> FrameSz:
    r = cls.scale_ratio(
      src,
      tgt,
    )
    dst = src * r 
    return dst
  

  @classmethod 
  def resize_img(
    cls,
    img: np.ndarray,
    tgt: FrameSz,
    keep_shape: bool=True,
    *args,
    **kwargs,
  ) -> np.ndarray:
    if keep_shape:
      src = FrameSz.from_img(
        img=img,
      )
      tgt = cls.resize_box(
        src,
        tgt,
      )
    dsize = (*tgt,)
    img = cv2.resize(
      src=img,
      dsize=dsize,
      interpolation=(
        cv2.INTER_LINEAR
      ),
      *args,
      **kwargs,
    )
    return img


  @classmethod 
  def save(
    cls,
    path: Path_,
    img: np.ndarray,
  ) -> NoReturn:
    PM.prepare_dir(path)
    cv2.imwrite(
      filename=path, 
      img=img,
    )


  @staticmethod
  def resize_bbox(
    img: np.ndarray=...,
    xyxy: np.ndarray=...,
    ratio: float=1.0,
  ) -> np.ndarray:
    # img.shape := (h, w, 3)
  
    assert ratio > 0
    assert img.ndim == 3
    assert 1 <= xyxy.ndim <= 2
    
    is_vector = (
      xyxy.ndim == 1
    )
    if is_vector:
      xyxy = np.expand_dims(
        xyxy,
        axis=0,
      )

    wh = img.shape[1::-1]

    delta = (
      xyxy[:, 2:]
      - xyxy[:, :2]
    ) * (ratio - 1.0) / 2

    np.maximum(
      xyxy[:, :2] - delta, 
      0, 
      out=xyxy[:, :2],
    )

    np.minimum(
      xyxy[:, 2:] + delta, 
      wh,
      out=xyxy[:, 2:],
    )
    
    if is_vector:
      xyxy = np.squeeze(
        xyxy,
        axis=0,
      )

    return xyxy


  @staticmethod 
  def crop(
    img: np.ndarray, 
    bbox: Tuple[
      int, 
      int, 
      int, 
      int,
    ],
    pad_size: int=0,
  ) -> np.ndarray:
    x0, y0, x1, y1 = bbox
    x0 -= pad_size
    y0 -= pad_size
    x1 += pad_size
    y1 += pad_size
    return img[y0:y1, x0:x1]


  @staticmethod
  def make_transparent(
    img: np.ndarray,
    orig_img: np.ndarray,
    transparency: float=.6,
  ) -> np.ndarray:
    t = transparency
    assert (
      img.shape 
      == orig_img.shape
    )
    assert 0 <= t <= 1
    img = cv2.addWeighted(
      src1=img, 
      alpha=1 - t, 
      src2=orig_img, 
      beta=t, 
      gamma=0,
    )
    return img


  @classmethod 
  def make_opaque(
    cls,
    img: np.ndarray,
    orig_img: np.ndarray,
    opacity: float=.4,
  ) -> np.ndarray:
    img = cls.make_transparent(
      img, 
      orig_img,
      1 - opacity,
    )
    return img