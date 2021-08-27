import typing 
import cmath



def fft(
  a: typing.List[int],
  inverse: bool=False,
) -> typing.NoReturn:
  n = len(a)
  if n == 1: return
  m = n // 2
  b = [0] * m
  c = [0] * m
  for i in range(m):
    b[i] = a[2 * i]
    c[i] = a[2 * i + 1]
  fft(b, inverse)
  fft(c, inverse)
  sign = -1 + 2 * inverse
  zeta = cmath.rect(1, sign * 2 * cmath.pi / n)
  x = 1
  for i in range(n):
    a[i] = b[i % m] + x * c[i % m]
    x *= zeta



def ifft(
  a: typing.List[int],
) -> typing.NoReturn:
  fft(a, inverse=1)
  for i in range(len(a)):
    a[i] /= len(a)
