import typing 
import numpy as np



class ModCumprod():
  def __call__(
    self,
    a: np.array,
  ) -> np.array:
    mod = self.__mod
    n = a.size
    m = int(n ** .5) + 1
    a = np.resize(a, (m, m))
    for i in range(m - 1):
      a[:, i + 1] *= a[:, i]
      a[:, i + 1] %= mod
    for i in range(m - 1):
      a[i + 1] *= a[i, -1]
      a[i + 1] %= mod
    return a.ravel()[:n]
 

  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__mod = mod
