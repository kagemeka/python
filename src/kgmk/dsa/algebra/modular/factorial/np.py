import typing
import numpy as np



class ModFactorial:
  def __call__(
    self, 
    n: int = 1 << 20,
  ) -> np.array:
    a = np.arange(n); a[0] = 1
    return self.cumprod(a)


  def cumprod(
    self, 
    a: np.array,
  ) -> np.array:
    m = self.__mod
    l = len(a)
    n = int(np.sqrt(l) + 1)
    a = np.resize(a, (n, n))
    for i in range(n-1):
      a[:, i + 1] *= a[:, i]
      a[:, i + 1] %= m
    for i in range(n-1):
      a[i + 1] *= a[i, -1]
      a[i + 1] %= m
    return np.ravel(a)[:l]


  def __init__(
    self,
    modulo: int,
  ) -> typing.NoReturn:
    self.__mod = modulo 
  

  def inv(
    self, 
    n: int = 1 << 20,
  ) -> np.array:
    a = np.arange(1, n + 1)
    m = self.__mod
    x = int(self(n)[-1])
    a[-1] = pow(x, m - 2, m)
    return self.cumprod(
      a[::-1],
    )[n::-1]