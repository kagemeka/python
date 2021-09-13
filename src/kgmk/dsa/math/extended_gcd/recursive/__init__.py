import typing 



class ExtGCD():
  def __call__(
    self, 
    a: int, 
    b: int,
  ) -> typing.Tuple[int, int, int]:
    if not b: return a, 1, 0
    q, r = divmod(a, b)
    g, s, t = self(b, r)
    return g, t, s - q * t