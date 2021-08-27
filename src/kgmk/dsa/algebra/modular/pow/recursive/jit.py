import numba as nb


@nb.njit
def mod_pow(
  x: int,
  n: int,
  mod: int,
) -> int:
  if n == 0: return 1
  y = mod_pow(x, n >> 1, mod)
  y = y * y % mod
  if n & 1: y = y * x % mod
  return y