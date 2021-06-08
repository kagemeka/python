from typing import (
  Type,
  Union,
)

Jsonizable: Type = Union[
  bool,
  dict,
  float,
  int,
  list,
  None,
  str,
]
