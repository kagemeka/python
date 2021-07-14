from ...bluestacks import (
  Emulator,
)

from ..constants import (
  Button,
)

from .base import BraveSouls


from time import sleep
import time 



from dataclasses import (
  dataclass,
)

from typing import List


class Quest(BraveSouls):

  def auto(self):
    self.click(
      Button.AUTO.value,
    )


  def next_(self):
    self.click(
      Button.CO_OP.value,
    )

  def run(self):
    ...

  def retry(self):
    self.click(
      Button.RETRY.value,
    )
  

  def close(self):
    self.click(
      Button.CLOSE.value,
    )
  


class Host(Quest):
  
  def call(self):
    self.click(
      Button.CALL_MEMBER.value,
    )
  

  def create(self):
    self.click(
      Button.CREATE_ROOM.value,
    )


  def confirm(self):
    self.click(
      Button.CONFIRM.value,
    )
  

  def close_confirm(self):
    self.confirm()

  
  def prepare(self):
    self.create()
    time.sleep(1<<3)
    self.call()
    time.sleep(1<<0)
    self.confirm()
    time.sleep(1<<1)
    self.close_confirm()


  def start(self):
    self.click(
      Button.START_QUEST.value,
    )
  

  


class Guest(Quest):

  def join(self):
    self.click(
      Button.JOIN.value,
    )

  def ready(self):
    self.click(
      Button.READY.value,
    )
  

  def prepare(self):
    self.message()
    time.sleep(1<<1)
    self.join()
    time.sleep(1<<3)
    self.ready()
  

  

  
@dataclass
class CoQuest:
  host: Host
  guests: List[Guest]
  
  def run(self):
    host = self.host
    guests = self.guests 

    for guest in guests:
      guest.close()

    host.prepare()
    time.sleep(1<<1)

    self.prepare_guests()

    time.sleep(1<<1)

    host.start()

    time.sleep(1<<4)

    for guest in guests:
      guest.auto()

    time.sleep(1<<7)

    host.retry()
    for guest in guests:
      guest.retry()

    time.sleep(1<<3)


  
  def prepare_guests(self):
    guests = self.guests

    for guest in guests:
      guest.message()
    
    time.sleep(1<<2)

    for guest in guests:
      guest.join()
    
    time.sleep(1<<3)

    for guest in guests:
      guest.ready()

    
