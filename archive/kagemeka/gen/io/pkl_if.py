from __future__ import (
  annotations,
)

import pickle

from . import (
  Path_,
)

from typing import (
  Any,
  Protocol,
  NoReturn,
)



from . import (
  Pkl,
)



class PklIF(
  Protocol,
):

  def to_pickle(
    self,
    path: Path_,
  ) -> NoReturn:
    Pkl.dump(
      obj=self,
      path=path,
    )


  @staticmethod
  def from_pickle(
    path: Path_,
  ) -> PklIF:
    obj = Pkl.load(
      path=path,
    )
    return obj