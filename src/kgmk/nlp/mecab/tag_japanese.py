import typing
import re 
import pandas as pd
import MeCab
from kgmk.nlp import (
  NormalizeJa,
)
from . import (
  Config,
)



class TagJapanese():
  __COLUMNS: typing.Final[
    typing.List[str]
  ] = [
    '表層形', 
    '品詞', 
    '品詞細分類1', 
    '品詞細分類2', 
    '品詞細分類3', 
    '活用型', 
    '活用形', 
    '原形', 
    '読み', 
    '発音',
  ]


  def __call__(
    self,
    s: str,
  ) -> pd.DataFrame:
    self.__s = NormalizeJa()(s)
    self.__parse()
    return pd.DataFrame(
      data=self.__parsed,
      columns=self.__COLUMNS,
    )
  

  def __init__(
    self,
    cfg: Config,
  ) -> typing.NoReturn:
    t = MeCab.Tagger(str(cfg))
    self.__tagger = t   


  def __parse(
    self,
  ) -> typing.NoReturn:
    ls = self.__tagger.parse(
      self.__s,
    ).split('\n')[:-2]
    *parsed, = map(
      lambda s: re.split(
        r'\t|,',
        s.strip(),
      ),
      ls,
    )
    self.__parsed = parsed
    if not parsed: return
    n = len(self.__COLUMNS)
    m = len(parsed[0])
    parsed[0] += (
      [None] * (n - m)
    )