import re
from typing import (
  List, 
  Iterable,
)

from ....gen import (
  vectorize,
)

from . import (
  NormForm,
)

from unicodedata import (
  normalize,
)


class TxtProc:
    
  @staticmethod
  @vectorize
  def rm_whitespaces(
    text: str,
  ) -> str:
    words = text.split()
    text = ' '.join(words)
    return text 
  

  @staticmethod 
  @vectorize 
  def tokenize(
    text: str,
  ) -> List[str]:
    return text.split()


  @staticmethod
  @vectorize
  def norm_txt(
    text: str,
    form: NormForm=(
      NormForm.NFKC,
    )
  ) -> str: 
    t = normalize(
      form=form.name, 
      unistr=text,
    )
    t = t.lower()
    return t 
    

  @staticmethod
  @vectorize
  def norm_num(
    text: str,
  ) -> str:
    t = re.sub(
      pattern=r'\d+', 
      repl='0', 
      string=text,
    )
    return t


  @classmethod
  @vectorize
  def norm(
    cls, 
    text: str,
  ) -> str:
    t = cls.norm_txt(text)
    t = cls.norm_num(t)
    return t


  @staticmethod 
  def regex_all(
    words: Iterable[str],
  ) -> str:
    patterns = (
      f'(?=.*{w})'
      for w in words
    )
    pattern = ''.join(
      patterns,
    )
    return pattern


  @staticmethod
  def regex_any(
    words: Iterable[str],
  ) -> str:
    pattern = '|'.join(words)
    return pattern