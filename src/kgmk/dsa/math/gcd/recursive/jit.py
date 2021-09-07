import numba as nb

@nb.njit
def gcd(a: int, b: int) -> int:
  return gcd(b, a % b) if b else a
