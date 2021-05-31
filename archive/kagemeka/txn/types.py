from dataclasses import (
  dataclass,
)

from ..gen import (
  DataClass,
)

from ipaddress import (
  ip_address,
  IPv4Address,
)


from typing import (
  Tuple,
)


@dataclass
class Addr(
  DataClass,
):
  host: str 
  port: int



@dataclass 
class IPAddrs:
  WILDCARD: IPv4Address = (
    ip_address('0.0.0.0')
  )

  LOOPBACK: IPv4Address = (
    ip_address('127.0.0.1')
  )

  # SUBNET = '192.xxx.xxx.xxx'
  # DOCKERSUB = '172.xxx.xxx.xxx'


Address = Tuple[str, int]