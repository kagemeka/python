from abc import ABCMeta, abstractmethod
import dataclasses 

@dataclasses.dataclass
class Base(metaclass=ABCMeta):
  ...
    

# print(BaseModel.__name__)
