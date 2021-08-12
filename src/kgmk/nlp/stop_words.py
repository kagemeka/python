import typing
from many_stop_words import (
  get_stop_words,
)



class Stopwords():
  @staticmethod
  def ja() -> typing.List[str]:
    return get_stop_words('ja')
  

  @staticmethod
  def en() -> typing.List[str]:
    return get_stop_words('en')


  @staticmethod
  def from_file(
    path: str,
  ) -> typing.List[str]:
    with open(
      path, 
      encoding='utf-8',
    ) as f:
      words = f.read().split()
    return words
  