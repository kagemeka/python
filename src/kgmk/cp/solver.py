from abc import (
  ABC,
  abstractmethod,
)
import typing



class Solver(
  ABC,
):
  def __call__(
    self,
  ) -> typing.NoReturn:
    self._prepare()
    self._solve()

  
  def __init__(
    self,
  ) -> typing.NoReturn:
    ...


  @abstractmethod
  def _prepare(
    self,
  ) -> typing.NoReturn:
    ...

  
  @abstractmethod
  def _solve(
    self,
  ) -> typing.NoReturn:
    ...