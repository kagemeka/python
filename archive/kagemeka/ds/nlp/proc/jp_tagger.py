import re
import MeCab 

import pandas as pd 
import numpy as np 
from typing import (
  List, 
  Iterable,
  Optional,
  Final,
)

import numpy as np 

from unicodedata import (
  normalize,
)


'''TODO
Pre Requisites

- mecab-ipadic-neologd
https://github.com/neologd/mecab-ipadic-neologd
'''


class JPTagger(
  MeCab.Tagger,
):
  columns: Final[
    List[str]
  ] = [
    'surf', 
    'pos', 
    'det0', 
    'det1', 
    'det2',
    'form0', 
    'form1', 
    'orig', 
    'pron0', 
    'pron1',
  ]
  
  def __init__(
    self,
    sys_dic: Optional[
      str
    ]=None,
    user_dics: Optional[
      Iterable[str]
    ]=None,
    *args,
    **kwargs,
  ):
    self.sys_dic = sys_dic 
    self.user_dics = user_dics
    opt = self.option 
    super().__init__(
      opt,
      *args,
      **kwargs,
    )

  
  @property
  def option(
    self,
  ) -> str:
    sys_dic = self.sys_dic 
    user_dics = self.user_dics
    if sys_dic is None:
      from . import DicCfg
      sys_dic = DicCfg.neologd
    opt = f'-d {sys_dic}'
    if not user_dics:
      return opt
    user_dics = ','.join(
      user_dics,
    )
    opt += f' -u {user_dics}'
    return opt


  def __call__(
    self,
    text: str,
  ) -> pd.DataFrame:
    try:
      tbl = self.parse_to_df(
        text,
      )
    except:
      tbl = pd.DataFrame(
        columns=self.columns,
      )
    return tbl
  

  def parse_to_df(
    self,
    text: str,
  ) -> pd.DataFrame:
    lines = self.parse(
      text,
    ).split('\n')[:-2]
    data = [
      self.flatten(l)
      for l in lines 
    ]
    tbl = pd.DataFrame(
      data=data,
      columns=self.columns,
    )
    tbl.replace(
      '*', 
      np.nan,
      inplace=True,
    )
    return tbl
  

  @staticmethod
  def flatten(
    line: str,
  ) -> List[str]:
    infos = re.split(
      pattern=',|\t', 
      string=line,
    )
    return infos  