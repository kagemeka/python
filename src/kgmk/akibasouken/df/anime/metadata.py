from dataclasses import (
  asdict,
)
import typing
import pandas as pd
from \
  kgmk.akibasouken.scrape \
  .anime \
import (
  Anime,
)


class MetadataToDF():

  def __call__(
    self,
    anime: Anime,
  ) -> pd.DataFrame:
    anime_id = anime.anime_id
    data = {
      'anime_id': anime_id,
      **asdict(anime.metadata),
    }
    return pd.Series(
      data,
    ).to_frame().T