import numpy as np 

from . import (
  Reader,
)


class NPReader(Reader):


  def line_ints(
    self,
  ) -> np.array:
    return np.fromstring(
      string=self.str_(),
      dtype=np.int64, 
      sep=' ',
    )


  def read_ints(
    self,
  ) -> np.array:
    return np.fromstring(
      string=(
        self().decode()
      ),
      dtype=np.int64, 
      sep=' ',
    )