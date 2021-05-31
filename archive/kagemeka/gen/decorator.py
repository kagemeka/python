import numpy as np 
from functools import (
  partial,
)

class vectorize(np.vectorize):
  
  def __get__(
    self, 
    obj, 
    objtype,
  ):
    p = partial(
      self.__call__, 
      obj,
    )
    return p