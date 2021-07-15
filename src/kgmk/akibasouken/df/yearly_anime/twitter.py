from \
  kgmk.akibasouken.scrape \
  .yearly_anime \
import (
  YearlyAnime,
)

from dataclasses import (
  asdict,
)
import typing
import pandas as pd
    


class TwitterToDF():

  def __call__(
    self,
    anime: YearlyAnime,
  ) -> pd.DataFrame:
    anime_id = anime.anime_id
    data = {
      'anime_id': anime_id,
      'twitter_username': (
        anime.twitter.username
      ),
    }
    return pd.Series(
      data,
    ).to_frame().T