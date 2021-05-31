'''
- Augmentation 
- Sequence (Time Series data)
- Single Value Regression.
'''

from typing import (
  Sequence,
)


import numpy as np



class AugSeqRegSingle:
  
  def __init__(
    self,
    data: np.ndarray,
    seq_len: int,
    delay: int=0,
  ):
    self.data = data 
    self.seq_len = seq_len
    self.delay = delay
  

  @property
  def sample_cnt(
    self,
  ) -> int:
    l = self.data.shape[0]
    s = self.seq_len 
    d = self.delay 
    n = l - s - d + 1
    return n
  

  @property
  def sample_len(
    self,
  ) -> int:
    return self.seq_len
  

  @property
  def y_index(
    self,
  ) -> np.ndarray:
    n = self.sample_cnt
    n = np.arange(n)
    s = self.seq_len 
    d = self.delay
    i = n + s + d - 1
    return i
  

  @property
  def x_index(
    self,
  ) -> np.ndarray:
    n = self.sample_cnt
    l = self.sample_len
    n = np.arange(n)
    m = np.arange(l)
    i = n[:, None] + m[None, :]
    return i
