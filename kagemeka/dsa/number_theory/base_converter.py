from typing import (
  List,
)


class BaseConverter:
  

  @staticmethod
  def to_nry(
    n: int,
    base: int,
  ) -> List[int]:
    assert abs(base) >= 2
    bits = []
    while True:
      n, r = divmod(n, base)
      if r < 0:
        n += 1
        r -= base
      bits.append(r)
      if n == 0:
        break
    return bits


  @staticmethod 
  def from_nry(
    bits: List[int],
    base: int,
  ) -> int:
    assert abs(base) >= 2
    n = 0 
    d = 1 
    for b in bits:
      n += d * b
      d *= base
    return n