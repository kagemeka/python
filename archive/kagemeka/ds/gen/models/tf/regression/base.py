from .. import TFBase

from tensorflow.keras import (
  losses, optimizers, metrics
)

from ..utils import LRSchedule 

class TFRegressor(TFBase):
  def __init__(self, **kwargs):
    super(TFRegressor, self) \
      .__init__(**kwargs)

    
    self.compile(
      loss=losses.MeanSquaredError(),
      optimizer=optimizers.Adam(
        learning_rate= \
          LRSchedule.inv_time_decay,
      ),
    )

  

  def call(self, x):
    x = super(
      TFRegressor, 
      self).call(x)
    return x
  ...

# losses.Reduction.