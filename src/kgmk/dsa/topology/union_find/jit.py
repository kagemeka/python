'''TODO
initialize a filled with -1.
a = [-1, -1, -1, ..., -1]
'''


import typing 
import numpy as np 
import numba as nb



@nb.njit
def find(
  a: np.array,
  u: int,
) -> int:
  if a[u] < 0: return u
  pu = find(a, a[u])
  a[u] = pu
  return pu


@nb.njit
def unite(
  a: np.array,
  u: int,
  v: int,
) -> typing.NoReturn:
  u = find(a, u)
  v = find(a, v)
  if u == v: return 
  if a[u] > a[v]: u, v = v, u
  a[u] += a[v]
  a[v] = u