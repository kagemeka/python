import typing 
import dataclasses 



T = typing.TypeVar('T')
@dataclasses.dataclass
class Monoid(typing.Generic[T]):
  fn: typing.Callable[[T, T], T]
  e: typing.Callable[[], T]
  commutative: bool = False 