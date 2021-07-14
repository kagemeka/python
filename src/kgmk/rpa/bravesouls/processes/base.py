from ...bluestacks import (
  Emulator,
)

from ..constants import (
  Button,
)

from abc import (
  ABC,
  ABCMeta,
)

class BraveSouls(
    Emulator,
    metaclass=ABCMeta):
    
  def message(self):
    self.click(
      Button.MESSAGE.value,
    )
  