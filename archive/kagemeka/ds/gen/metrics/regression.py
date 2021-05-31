from \
  __future__ \
import (
  annotations,
)

import \
  __future__ 


__future__.

from sklearn.metrics import (
  mean_absolute_error, 
  mean_squared_error, 
  r2_score,
)
from sklearn import (
  metrics,
)

from dataclasses import (
  dataclass,
  astuple,
  asdict,
  field,
)

from .base import (
  Metric,
)


@dataclass
class RegressionMetric(
  Metric,
):
  mae: float = None
  mse: float = None
  r2score: float = None

    
  @classmethod 
  def calc(
    cls,
    y,
    pred,
  ):
    return cls(
      mae=mean_absolute_error(
        y, 
        pred,
      ),
      mse=mean_squared_error(
        y, 
        pred,
      ),
      r2score=r2_score(
        y, 
        pred,
      ),
    )


def _test():
  import numpy as np 
  a = np.array([1, 0, 1, 0])
  b = np.array([1, 1, 1, 0])

  c = RegressionMetric()
  c = c(a, b)
  print(c)


if __name__ == '__main__':
  _test()