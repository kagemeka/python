from abc import (
  ABC,
)

from typing import (
  Tuple,
)
from imblearn.under_sampling \
  import(
  RandomUnderSampler,
)
from imblearn.over_sampling \
  import (
  RandomOverSampler,
)

import numpy as np 

from sklearn.model_selection \
  import (
  train_test_split,
)

class SamplingIF(ABC):
  def __init__(self):
    super().__init__(
      random_state=0,
    )
  
  def __call__(
    self,
    *args,
    **kwargs,
  ):
    return self.sample_(
      *args,
      **kwargs,
    )

  def sample_(
    self,
    y: np.ndarray,
  ) -> Tuple[
    np.ndarray,
    np.ndarray,
  ]:
    assert y.ndim == 1
    i = np.arange(
      y.size,
    ).reshape(-1, 1)
    return self.fit_resample(
      i,
      y,
    )


class UnderSampler(
  SamplingIF,
  RandomUnderSampler,
):
  ...



class OverSampler(
  SamplingIF,
  RandomOverSampler,
):
  ...

  