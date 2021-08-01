import numba as nb


@nb.njit
def bit_length(n: int) -> int:
  c = 0
  while n: n >>= 1; c += 1
  return c
