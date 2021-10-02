import numba as nb


@nb.njit 
def bit_length(n: int) -> int:
  l = 0
  while 1 << l <= n: l += 1
  return l
