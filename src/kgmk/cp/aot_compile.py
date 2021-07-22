'''
This is a snippet.
You cannot use this via importing.
'''

import numpy as np
import typing


def foo(
  a: np.array,
) -> np.array: ...


def solve(
  n: int, 
  m: int,
) -> typing.NoReturn: 
  ...
  a = np.arange(10)
  foo(a)
  ...


def main() -> typing.NoReturn: 
  ...
  solve(1, 2)


# TODO cut below


import sys

if (
  sys.argv[-1] 
  == 'ONLINE_JUDGE'
):
  '''TODO'''
  from numba import njit, i8
  foo = njit(foo)
  fn = solve 
  signature = (i8, i8)
  ''''''

  from numba.pycc import CC
  cc = CC('my_module')
  cc.export(
    fn.__name__, 
    signature,
  )(fn)
  cc.compile()
  exit(0)


from my_module import solve
main()