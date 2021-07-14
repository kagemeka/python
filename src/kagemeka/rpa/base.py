import pyautogui
from abc import (
  ABC,
  abstractmethod,
)

class RPA(ABC):

  @staticmethod
  def click(**kwargs):
    pyautogui.click(**kwargs)

  

  @abstractmethod 
  def run(self, **kwargs):
    ...

  

