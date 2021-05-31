from typing import (
  Final,
  ClassVar,
  final,
)

from ....gen import (
  DataClass,
  Reader,
)

from subprocess import (
  Popen,
  PIPE,
)

from dataclasses import (
  dataclass,
)

from . import (
  JPTagger as JPT,
)



@dataclass
class DicCfg(
  DataClass,
):

  neologd_rt: ClassVar[
    str
  ] = (
    '/usr/lib/'
    'x86_64-linux-gnu/'
    'mecab/dic'
  )
  
  neologd: str = (
    f'{neologd_rt}/'
    'mecab-ipadic-neologd'
  )

  @final
  @staticmethod
  def neologd_root() -> str:
    cmd = (
      'echo '
      '`mecab-config --dicdir`'
    )
    stdout = Popen(
      cmd,
      shell=True,
      stdout=PIPE,
    ).stdout
    reader = Reader(
      src=stdout,
    )
    with reader as r:
      root = r.str_()
    return root
