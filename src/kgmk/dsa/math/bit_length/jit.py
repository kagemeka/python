import numba as nb


@nb.njit
def bit_length(n: int) -> int:
  l = 0
  while n: 
    l += 1
    n >>= 1
  return l
