import numba as nb 

@nb.njit((nb.i8, ), cache=True)
def n_choose_2(n: int) -> int:
  return n * (n - 1) // 2 if n >= 2 else 0