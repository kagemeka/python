from pprint import pprint

from . import (
  DataClass,
)

from dataclasses import (
  dataclass,
)

from typing import (
  final,
  List,
)

from torch.cuda import (
  device_count,
  current_device,
  get_device_name,
  is_available,
)

import tensorflow as tf

from tensorflow \
  .config import (
  list_physical_devices,
)

from tensorflow \
  .python \
  .eager \
  .context import (
  PhysicalDevice,
)


@final
@dataclass
class PTCudaProperties(
  DataClass,
):
  device_count: int = None 
  current_device: int = None 
  device_name: str = None
  is_available: bool = False

  
  @classmethod 
  def check(
    cls,
  ):
    device = current_device()
    count = device_count()
    name = get_device_name(
      device,
    )
    available = is_available()

    prop = cls(
      device_count=count,
      current_device=device,
      device_name=name,
      is_available=available,
    )
    return prop


@final
@dataclass
class TFProperties(
  DataClass,
):
  gpus: List[
    PhysicalDevice
  ] = None

  @classmethod 
  def check(
    cls,
  ):
    (
      gpus
    ) = list_physical_devices(
      'GPU',
    )
    prop = cls(
      gpus=gpus,
    )
    return prop 


class GPUTest:
  
  @staticmethod
  def tf():
    prop = TFProperties.check()
    pprint(prop.dic)

  
  @staticmethod 
  def pt():
    prop = (
      PTCudaProperties
      .check()
    )
    pprint(prop.dic)
 

  def __call__(self):
    self.pt()
    self.tf()