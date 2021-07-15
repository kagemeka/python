import typing
from tqdm import (
  tqdm,
)
from . import (
  ScrapeFreeComic,
  FreeComic,
)



class ScrapeFreeComics():
  def __call__(
    self,
    ids: typing.List[int],
  ) -> typing.Iterator[
    FreeComic
  ]:
    fn = ScrapeFreeComic()
    for id_ in tqdm(ids):
      yield fn(id_)
      
    