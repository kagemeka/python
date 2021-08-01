from ..gcd import (
  GCD,
)
# TODO cut below



class LCM():
  def __call__(
    self,
    a: int,
    b: int,
  ) -> int:
    return a // GCD()(a, b) * b