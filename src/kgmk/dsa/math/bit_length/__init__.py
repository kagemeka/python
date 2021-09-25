class BitLength():
  def __call__(
    self,
    n: int,
  ) -> int:
    l = 0
    while n: 
      l += 1
      n >>= 1
    return l
