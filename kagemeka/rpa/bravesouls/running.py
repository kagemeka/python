from ..bluestacks import (
  Runner,
  Resolution,
)


from .processes.co_op import (
  CoQuest,
  Host,
  Guest,
)

import time 

class CoRunner(Runner):
  def __init__(
      self,
      **kwargs):

    super(
      CoRunner,
      self,
    ).__init__(**kwargs)
  

  def create_unit(
      self, host_id):
    
    guests = []
    for i in range(self.n):
      if i == host_id:
        host = Host(
          self.upper_left(i),
          self.em_size,
        )
        continue      
      guest = Guest(
        self.upper_left(i),
        self.em_size,
      )
      guests.append(guest)


    unit = CoQuest(
      host,
      guests,
    )
    return unit 


  def run(self):
    i = 0
    for i in range(1<<8):
      i %= self.n
      if i == self.n - 1:
        continue
      unit = \
        self.create_unit(i)
      unit.run()
      


