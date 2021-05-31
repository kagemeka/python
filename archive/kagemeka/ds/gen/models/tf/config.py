from enum import (
  Enum,
)

from dataclasses import (
  dataclass,
)


from kagemeka \
  .general \
  .types import (
  DataClass,
)


@dataclass
class TFModelConfig(
  DataClass,
):
  path: str = None
  weights_only: bool = True
  epochs: int = 1 << 0
  batch_size: int = None
  steps_per_epoch: int = None
  use_multiprocessing: bool = (
    False
  )



  