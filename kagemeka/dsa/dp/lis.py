from bisect import (
  bisect_left,
)


from typing import (
  Any,
)



class LIS:


  def __init__(
    self,
    inf: Any=float('inf'),
  ):
    self.inf = inf


  def __call__(
    self,
    a: list,
  ):
    inf = self.inf
    lis = [inf] * len(a)
    for x in a:
      i = bisect_left(lis, x)
      lis[i] = x
    i = bisect_left(lis, inf)
    return lis[:i]