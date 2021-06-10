from . import TFRegressor 

from tensorflow.keras import (
  layers,
)

class TFLSTMRegressor(TFRegressor):
  def __init__(self, **kwargs):
    super(
      TFLSTMRegressor, 
      self).__init__(*kwargs)


  
  def call(self, x):
    x = super(
      TFLSTMRegressor, 
      self,
    ).call(x)
    x = self.lstm(x)
    x = self.fc6(x)
    x = self.dropout(x)
    x = self.to_out(x)
    return x 
    
  ...

