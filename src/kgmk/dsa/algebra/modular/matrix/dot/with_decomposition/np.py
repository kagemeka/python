import numpy as np 
import typing



class ModMatrixDot():  
  def __call__(
    self,
    a: np.ndarray,
    b: np.ndarray,
  ) -> np.ndarray:
    mod = self.__mod
    N: typing.Final[int] = 15
    MASK: typing.Final[int] = (1 << N) - 1
    assert (
      np.ndim(a) == np.ndim(b) == 2
      and a.shape[1] == b.shape[0] 
    )
    a0, a1 = a & MASK, a >> N
    b0, b1 = b & MASK, b >> N 
    c0 = np.dot(a0, b0) % mod 
    c2 = np.dot(a1, b1) % mod 
    c1 = np.dot(a0 + a1, b0 + b1) - c0 - c2
    c1 %= mod 
    c = (c1 << N * 2) + (c1 << N) + c0
    return c % mod


  def __init__(
    self,
    mod: int,
  ) -> typing.NoReturn:
    self.__mod = mod 