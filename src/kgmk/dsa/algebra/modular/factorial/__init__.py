import typing



class ModFactorial():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    a = list(range(n))
    a[0] = 1
    self.__cumprod(a)
    return a


  def __cumprod(
    self,
    a: typing.List[int],
  ) -> typing.NoReturn:
    for i in range(len(a) - 1):
      a[i + 1] *= a[i]
      a[i + 1] %= self.__mod


  def __init__(
    self,
    modulo: int,
  ) -> typing.NoReturn:
    self.__mod = modulo
  

  def inv(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    b = self(n)
    a = list(range(1, n + 1))
    m = self.__mod
    x = pow(b[-1], m - 2, m)
    a[-1] = x
    a.reverse()
    self.__cumprod(a)
    return a[::-1]