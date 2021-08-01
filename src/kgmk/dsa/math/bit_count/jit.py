import numba as nb


@nb.njit
def bit_count(n: int) -> int:
  c = 0 
  while n:
    c += n & 1
    n >>= 1
  return c
  