from __future__ import (
  annotations,
)
from .read_stdin import (
  ReadStdin,
)
from .solver import (
  Solver,
)
# TODO cut below



import typing


class Problem(
  Solver,
):
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__read = ReadStdin()


  def _prepare(
    self,
  ) -> typing.NoReturn:
    ... 


  def _solve(
    self,
  ) -> typing.NoReturn:
    ...


def main():
  p = Problem()
  t = 1
  # t = ReadStdin().int()
  for _ in range(t): p()


if __name__ == '__main__':
  main()