import numpy as np 
import cv2 
from .config import (
  FeatureParams,
  LKParams,
  OpticalFlowCofing,
)


class OpticalFlow:
  def __init__(
    self,
    config: OpticalFlowCofing,
  ):
    
    feature_params = (
      config
      .feature_params
      .asdict()
    )
    lk_params = (
      config
      .lk_params
      .asdict()
    )

    color = np.random.randint(
      0, 255, (100, 3),
    )

    (
      self.feature_params,
      self.lk_params,
      self.color,
      self.p0,
      self.mask,
      self.gray_img0,
    ) = (
      feature_params,
      lk_params,
      color,
      None,
      None,
      None,
    )

  
  @classmethod 
  def grayscale(
    cls,
    img,
  ):
    img = cls.gain_contrast(
      img,
    )
    gray_img = cv2.cvtColor(
      img,
      cv2.COLOR_BGR2GRAY,
    )
    return gray_img 


  @staticmethod 
  def gain_contrast(
    img,
  ):

    alpha = 3.0
    img = alpha * img 
    return np.clip(
      img,
      0,
      (1<<8) - 1,
    ).astype(np.uint8)
  

  def init_features(
    self,
    img,
  ): 
    gray_img = self.grayscale(
      img
    )
    self.p0 = (
      cv2.goodFeaturesToTrack(
        gray_img,
        **self.feature_params,
      )
    )
    self.mask = np.zeros_like(
      img,    
    )

    self.gray_img0 = gray_img


  def handle(
    self,
    img,
  ):
    if (
      self.gray_img0 is None
    ):
      self.init_features(
        img,
      )
      return img

    return self.flow(img)


  def add_line(
    self,
    id_,
    **kwargs,
  ):
    color = (
      self.color[id_].tolist()
    )
    self.mask = cv2.line(
      **kwargs,
      img=self.mask,
      color=color,
      thickness=2,
    )

  
  def add_circle(
    self,
    id_,
    **kwargs,
  ):
    color = (
      self.color[id_].tolist()
    )
    return cv2.circle(
      **kwargs,
      radius=5,
      color=color,
      thickness=-1,
    )


  def next_(
    self,
    img,
  ):
    gray_img = self.grayscale(
      img,
    )
    p, st, err = (
      cv2
      .calcOpticalFlowPyrLK(
        prevImg=self.gray_img0,
        nextImg=gray_img,
        prevPts=self.p0,
        nextPts=None,
        **self.lk_params,
      )
    )
    self.gray_img0 = gray_img
    return p, st, err


  def flow(
    self,
    img,
  ):
    p, st, err = self.next_(
      img,
    )

    good_new = p[st==1]
    good_old = self.p0[st==1]

    for i, (new, old) in (
      enumerate(
        zip(
          good_new,
          good_old,
        )
      )
    ):
      a, b = new.ravel()
      c, d = old.ravel()
      self.add_line(
        id_=i,
        pt1=(a, b),
        pt2=(c, d),
      )

      img = self.add_circle(
        img=img,
        id_=i,
        center=(a, b), 
      )
    
    img = cv2.add(
      img, 
      self.mask,
    )

    self.p0 = good_new.reshape(
      -1, 1, 2,
    )

    return img

  def __call__(
    self, 
    *args,
    **kwargs,
  ):
    return self.handle(
      *args,
      **kwargs,
    )
    

def _test():
  feature_params = (
    FeatureParams()
  )
  lk_params = LKParams()
  cfg = OpticalFlowCofing(
    feature_params,
    lk_params,
  )
  of = OpticalFlow(
    config=cfg,
  )
  

if __name__ == '__main__':
  _test()