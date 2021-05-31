from typing import Tuple 

from sklearn.metrics import (
  accuracy_score, 
  recall_score, 
  precision_score, 
  f1_score,
)


from dataclasses import (
  dataclass,
  astuple,
  asdict,
  field,
)


from .base import Metric

@dataclass
class ClassificationMetric(
  Metric,
):
  accuracy: float = None 
  precision: float = None 
  recall: float = None 
  f1score: float = None 
  auc: float = None

  @classmethod 
  def calc(
    cls,
    y,
    pred,
  ):
    return cls(
      accuracy=accuracy_score(
        y,
        pred,
      ),
      precision=(
        precision_score(
          y,
          pred,
        )
      ),
      recall=recall_score(
        y,
        pred,
      ),
      f1score=f1_score(
        y,
        pred, 
      ),
    )
    

def _test():
  import numpy as np 
  a = np.array([1, 0, 1, 0])
  b = np.array([1, 1, 1, 0])

  c = ClassificationMetric()
  c = c(a, b)
  print(c)


if __name__ == '__main__':
  _test()