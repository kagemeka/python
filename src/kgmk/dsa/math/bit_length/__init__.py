class BitLength():
  def __call__(
    self,
    n: int,
  ) -> int:
    c = 0 
    while n: n >>= 1; c += 1
    return c