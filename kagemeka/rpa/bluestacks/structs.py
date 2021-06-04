from dataclasses import (
  dataclass
)

from .. import (
  Vector2D,
)

@dataclass
class Resolution(Vector2D):
  x: int = 640
  y: int = 360
