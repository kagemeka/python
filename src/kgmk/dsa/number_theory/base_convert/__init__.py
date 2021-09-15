import typing



class BaseConvert:
  def __call__(
    self,
    n: typing.List[int],
    from_: int,
    to: int,
  ) -> typing.List[int]:
    n = self.from_nry(n, from_)
    return self.to_nry(n, to)
    

  @staticmethod 
  def from_nary(
    bits: typing.List[int],
    base: int,
  ) -> int:
    assert abs(base) >= 2
    n = 0 
    d = 1 
    for b in bits:
      n += d * b
      d *= base
    return n


  @staticmethod
  def to_nary(
    n: int,
    base: int,
  ) -> typing.List[int]:
    assert abs(base) >= 2
    bits = []
    while True:
      n, r = divmod(n, base)
      if r < 0:
        n += 1
        r -= base
      bits.append(r)
      if n == 0: break
    return bits