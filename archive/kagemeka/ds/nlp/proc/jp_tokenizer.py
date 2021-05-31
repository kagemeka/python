
import pandas as pd 

from typing import (
  Iterable,
  Optional,
)

from ....gen import (
  vectorize,
)

from . import (
  TxtProc,
  JPTagger,
)



class JPTokenizer(
  TxtProc,
):

  def __init__(
    self, 
    pos: Optional[
      Iterable[str]
    ]=None,
    sys_dic: Optional[
      str
    ]=None,
    user_dics: Optional[
      Iterable[str]
    ]=None,
    orig: bool=True,
  ):
    self.tagger = JPTagger(
      sys_dic=sys_dic,
      user_dics=user_dics,
    )
    self.pos = pos
    self.orig = orig


  def tokenize(
    self,
    text: str,
  ) -> str:
    tbl = self.get_df(text)
    words = self.get_words(
      tbl=tbl,
    )
    text = ' '.join(words)
    return text
  
  
  @vectorize
  def __call__(
    self,
    text: str,
  ) -> str:
    return self.tokenize(text)


  def get_words(
    self,
    tbl: pd.DataFrame,
  ) -> pd.Series:
    res = tbl.surf 
    return_orig = self.orig 
    if return_orig:
      ok = tbl.orig.notna()
      res.loc[ok] = (
        tbl.orig.loc[ok]
      )
    return res


  def get_df(
    self,
    text: str,
  ) -> pd.DataFrame:
    tbl = self.tagger(text)
    tbl = self.sieve(tbl)
    return tbl


  def sieve(
    self, 
    tbl: pd.DataFrame,
  ) -> pd.DataFrame:
    pos = self.pos
    if pos is None:
      return tbl
    cols = [
      'pos', 
      'det0',
    ]
    ok = tbl[cols].isin(
      self.pos,
    ).any(axis=1)
    return tbl.loc[ok]