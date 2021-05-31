from dataclasses import (
  dataclass,
  asdict,
  astuple,
)
from typing import (
  Tuple,
)

import cv2



'''TODO 
violate coding style due to opencv parameters.
'''

@dataclass
class FeatureParams:
  maxCorners: int = 100 
  qualityLevel: float = 0.3
  minDistance: int = 7
  blockSize: int = 7

  def asdict(self):
    return asdict(self)
  

@dataclass
class LKParams:
  winSize: Tuple[int, int] = (
    15, 15,
  )
  maxLevel: int = 2
  criteria: Tuple[
    int,
    int,
    float,
  ] = (
    cv2.TERM_CRITERIA_EPS 
    | cv2.TERM_CRITERIA_COUNT,
    10, 
    0.03,
  )
  
  def asdict(self):
    return asdict(self)


@dataclass
class OpticalFlowCofing:
  feature_params: FeatureParams
  lk_params: LKParams
