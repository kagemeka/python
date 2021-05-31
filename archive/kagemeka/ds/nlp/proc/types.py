from enum import (
  Enum,
  unique,
  auto,
)



@unique 
class NormForm(
  Enum,
):
  NFC = auto()
  NFKC = auto()
  NFD = auto() 
  NFKD = auto()