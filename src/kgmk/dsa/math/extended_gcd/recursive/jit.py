import typing
import numba as nb 


@nb.njit((nb.i8, nb.i8), cache=True)
def ext_gcd(a: int, b: int) -> typing.Tuple[int, int, int]:
  if not b: return a, 1, 0
  g, s, t = ext_gcd(b, a % b)
  return g, t, s - a // b * t