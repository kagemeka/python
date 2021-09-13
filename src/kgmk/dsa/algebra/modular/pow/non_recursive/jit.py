import numba as nb 


@nb.njit((nb.i8, nb.i8, nb.i8), cache=True)
def mod_pow(x: int, n: int, mod: int) -> int:
  y = 1
  while n:
    if n & 1: y = y * x % mod 
    x = x * x % mod 
    n >>= 1
  return y