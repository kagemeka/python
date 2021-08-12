import dataclasses
import typing



@dataclasses.dataclass 
class Config():
  sys_dic: typing.Optional[
    str
  ] = None
  user_dics: typing.Optional[
    typing.List[str]
  ] = None


  def __str__(
    self,
  ) -> str:
    opts = {}
    if self.sys_dic:
      opts['-d'] = self.sys_dic
    
    if self.user_dics:
      opts['-u'] = ','.join(
        self.user_dics,
      )
    return ' '.join(
      f'{k} {v}'
      for k, v in opts.items()
    )