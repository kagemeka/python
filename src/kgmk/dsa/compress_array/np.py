import numpy as np
import typing 



class CompressArray():
  def retrieve(
    self,
    i: int,
  ) -> int:
    return self.__v[i]
  
  def __call__(
    self,
    a: np.array,
  ) -> np.array:
    v = np.unique(a)
    self.__v = v
    i = np.searchsorted(v, a)
    return i