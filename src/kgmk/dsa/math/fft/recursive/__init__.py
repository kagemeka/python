import typing 
import cmath



class FFT():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    self.__dft(a)
    n = len(a)
    if self.__inv:
      for i in range(n): a[i] /= n
       
  
  def __dft(
    self,
    a: typing.List[int],
  ) -> typing.NoReturn:
    n = len(a)
    assert 1 << (n.bit_length() - 1) == n
    if n == 1: return
    m = n // 2
    b = [0] * m
    c = [0] * m
    for i in range(m):
      b[i] = a[2 * i]
      c[i] = a[2 * i + 1]
    self.__dft(b)
    self.__dft(c)
    sign = -1 + 2 * self.__inv
    zeta = cmath.rect(1, sign * 2 * cmath.pi / n)
    x = 1
    for i in range(n):
      a[i] = b[i % m] + x * c[i % m]
      x *= zeta

  
  def __init__(
    self,
    inverse: bool=False
  ) -> typing.NoReturn:
    self.__inv = inverse