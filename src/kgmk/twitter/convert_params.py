import typing
from typing import (
  Dict,
  Optional,
)
import dataclasses
from dataclasses import (
  fields,
)



@dataclasses.dataclass
class Param():
  name: str
  string: str



class Params(
  typing.Protocol,
):

  __dataclass_field__: (
    typing.ClassVar[Dict[
      str,
      dataclasses.Field,
    ]]
  )

  NAME: Optional[str]
  


class ConvertParams():
  def __call__(
    self,
    params: Params,
  ) -> Param:
    ls = self.__dfs(params)
    s = ','.join(ls)
    name = params.NAME
    return Param(name, s)

  
  @classmethod
  def __dfs(
    cls,
    params: Params,
  ):
    ls = []
    for f in fields(params):
      f = f.name
      v = getattr(params, f)
      if v == False: continue
      if v == True:
        ls.append(f); continue
      ls += [
        f if s == 'self_'
        else f'{f}.{s}'  
        for s in cls.__dfs(v)
      ]
    return ls
    