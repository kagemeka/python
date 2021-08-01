class GCD():
  def __call__(
    self,
    a: int,
    b: int,
  ) -> int:
    if b == 0: return a
    return self(b, a % b)

