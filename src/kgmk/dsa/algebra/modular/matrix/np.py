import typing
import numpy as np



class ModMatrix():  
  def __init__(
    self,
    modulo: int,
  ) -> typing.NoReturn:
    self.__mod = modulo 


  def dot(
    self,
    a: np.ndarray,
    b: np.ndarray,
  ) -> np.array:
    m = self.__mod
    N: typing.Final[int] = 15
    MASK: (
      typing.Final[int]
    ) = (1 << N) - 1
    # decompose with base 2^N
    a0, a1 = a & MASK, a >> N
    b0, b1 = b & MASK, b >> N 
    c0 = np.dot(a0, b0) % m
    c2 = np.dot(a1, b1) % m
    c1 = np.dot(
      a0 + a1, 
      b0 + b1,
    ) - c0 - c2
    c1 %= m
    c = c0
    c += c1 << N
    c += c2 << N * 2
    return c % m


  def pow(
    self,
    a: np.ndarray,
    n: int,
  ) -> np.ndarray:
    if n == 0:
      return np.identity(
        a.shape[0],
        dtype=np.int64,
      ) 
    x = self.pow(a, n >> 1)
    x = self.dot(x, x)
    if n & 1: 
      x = self.dot(x, a)
    return x