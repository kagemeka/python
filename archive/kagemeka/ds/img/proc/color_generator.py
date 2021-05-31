
from typing import (
  final,
)

@final
class ColorGenerator:
  PALETTE = (
    (1 << 11) - 1, 
    (1 << 15) - 1,
    (1 << 20) - 1,
  )

  def __call__(
    self, 
    id_: int,
  ):
    n = id_
    color = tuple(
      int(
        p 
        * (n ** 2 - n + 1)
        % ((1 << 8) - 1)
      )
      for p in self.PALETTE
    )
    return color 