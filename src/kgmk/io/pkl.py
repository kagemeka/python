import pickle

from . import (
  Path_,
)

from typing import (
  Any,
)



class Pkl:

  @staticmethod
  def dump(
    obj: Any,
    path: Path_,
  ) -> None:
    with open(
      file=path,
      mode='wb',
    ) as f:
      pickle.dump(
        obj=obj,
        file=f,
      )
  

  @staticmethod
  def load(
    path: Path_,
  ) -> Any:
    with open(
      file=path,
      mode='rb',
    ) as f:
      obj = pickle.load(
        file=f,
      )
    return obj
  