from typing import (
  final,
)

from enum import (
  Enum,
  IntFlag,
  Flag,
  auto,
  unique,
)

import enum 


@final
class Status(IntFlag):
  DEACTIVE = auto()
  ACTIVE = auto()
  PAUSED = auto()
  SUSPENDED = auto()
  WAITING = auto()
  PENDING = auto()



class FileFormat(Enum):
  PING = auto()
  PNG = PING
  JPEG = auto()
  JPG = JPEG
  MP4 = auto()
  AVI = auto()
  MOV = auto()
  MP3 = auto()
  WAV = auto()
  CSV = auto()
  EXCEL_WORKBOOK = auto()
  XLSX = EXCEL_WORKBOOK
  WILDCARD = auto()
  PICKLE = auto()
  DB = auto()
  SQL = DB
