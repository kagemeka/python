class BitCount():
  def __call__(
    self,
    n: int,
  ) -> int:
    c = 0 
    while n:
      c += n & 1
      n >>= 1
    return c
    