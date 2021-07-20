import functools
import typing



class Accumulate:
  @staticmethod 
  def __call__(
    func: typing.Callable,
    identity: int,
  ):
    def fn(
      a: typing.Iterable[int],
    ) -> int:
      return functools.reduce(
        func,
        a,
        identity,
      )
    return fn