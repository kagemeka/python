from kagemeka \
  .general \
  .io_ \
  .pickle_interface import (
  PickleIF,
)

from sklearn \
  .preprocessing import (
  MinMaxScaler, 
  StandardScaler, 
  Normalizer,
)

class MinMaxScaler_(
  MinMaxScaler, 
  PickleIF,
):
  ...



class StandardScaler_(
  StandardScaler,
  PickleIF,
):
  ...

