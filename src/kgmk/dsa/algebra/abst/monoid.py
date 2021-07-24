import dataclasses
import typing


T = typing.TypeVar('T')

@dataclasses.dataclass
class Monoid(
  typing.Generic[T],
):
  fn: typing.Callable[
    [T, T],
    T,
  ]
  e: T