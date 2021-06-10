from operator import xor, or_

from functools import reduce


from typing import (
  Iterable,
)

class Accumulation:
  @staticmethod 
  def cummulative(
    function,
    identity,
  ):
    def f(sequence: Iterable):
      return reduce(
        function,
        sequence,
        identity, 
      )
    
    return f



xor = Accumulation.cummulative(
  xor, 0,
)
or_ = Accumulation.cummulative(
  or_, 0,
)
