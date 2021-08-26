import numpy as np 
import typing



class ModMatrixDot():  
  def __call__(
    self,
    a: np.ndarray,
    b: np.ndarray,
  ) -> np.ndarray:
    mod = self.__mod
    assert (
      np.ndim(a) == np.ndim(b) == 2
      and a.shape[1] == b.shape[0] 
    )
    c = a[:, None, :] * b.T[None, ...] % mod
    return c.sum(axis=-1) % mod 


  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__mod = mod 