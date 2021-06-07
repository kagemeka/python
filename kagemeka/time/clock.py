import time 

from dataclasses import (
  dataclass,
)



@dataclass
class Clock:

  value: float = time.time()


  def __call__(
    self,
  ) -> float:
    return self.value
  

  @staticmethod
  def now() -> float:
    return time.time()

  
  def stamp(self) -> float:
    self.value = self.now()
    return self()


  @property 
  def dt(self) -> float:
    t0 = self.value 
    t1 = self.stamp()
    return t1 - t0



def _test():
  clk = Clock()
  time.sleep(1)
  dt = clk.dt 
  print(dt)