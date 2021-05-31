from \
  abc \
import (
  ABC, 
  abstractclassmethod,
)


# @dataclass
class Metric(ABC):
  def __call__(
    self,
    *args,
    **kwargs,
  ):
    return self.__class__.calc(
      *args,
      **kwargs,
    ) 
  

  @abstractclassmethod
  def calc(
    cls,
    y,
    pred,
  ):
    ...
