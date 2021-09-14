import typing 



class ExtGCD():
  def __call__(
    self, 
    a: int, 
    b: int,
  ) -> typing.Tuple[int, int, int]:
    if not b: return a, 1, 0
    g, s, t = self(b, a % b)
    return g, t, s - a // b * t