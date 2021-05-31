from \
  ..gen.io.reading.std_reader \
import (
  StdReader,
)


# cut below


from abc import (
  ABC,
  abstractmethod,
)


class Solver(ABC):


  def __init__(self):
    self.reader = StdReader()


  def __call__(
    self,
  ):
    self.prepare()
    self.solve()


  @abstractmethod
  def prepare(self):
    ...
      

  @abstractmethod 
  def solve(self):
    ...



import numpy as np


class Problem(
  Solver,
):


  def prepare(self):
    ...


  def solve(self):
    ...