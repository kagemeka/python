import numba as nb


@nb.njit((nb.i8, nb.i8), cache=True)
def gcd(a: int, b: int) -> int:
  while b: a, b = b, a % b
  return a