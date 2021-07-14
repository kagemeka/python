import typing
from dataclasses import (
  fields,
)
from . import (
  Params,
)


class EnableAllParams():
  def __call__(
    self,
    params: Params,
  ) -> typing.NoReturn:
    for f in fields(params):
      f = f.name
      v = getattr(params, f)
      if type(v) != bool:
        self(v)
        continue
      setattr(params, f, True)
    