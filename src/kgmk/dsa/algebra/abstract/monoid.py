import dataclasses
import typing



T = typing.TypeVar('T')
@dataclasses.dataclass 
class Monoid(
  typing.Generic[T],
):
  f: typing.Callable[[T, T], T]
  e: typing.Callable[[], T]
  commutative: bool = False