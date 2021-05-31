from enum import Enum 

from .. import (
  Point,
)


class Button(Enum):
  CREATE_ROOM = Point(
    0.365,
    0.530,
  )

  CALL_MEMBER = Point(
    0.040,
    0.325,
  )

  CONFIRM = Point(
    0.63,
    0.68,
  )

  MESSAGE = Point(
    0.88, 0.05
  )

  PUBLIC = Point(
    0.85,
    0.17,
  )

  JOIN = Point(0.2, 0.85)

  READY = Point(0.8, 0.93)

  START_QUEST = Point(
    0.8, 0.93,
  )

  AUTO = Point(0.31, 0.93)

  RETRY = Point(0.17, 0.93)

  CO_OP = Point(0.83, 0.93)

  CLOSE = Point(0.5, 0.75)