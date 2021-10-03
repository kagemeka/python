import numba as nb


@nb.njit
def bit_count(n: int) -> int:
  cnt = 0 
  while n:
    cnt += n & 1
    n >>= 1
  return cnt
  