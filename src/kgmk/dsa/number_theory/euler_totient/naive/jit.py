import numba as nb




@nb.njit((nb.i8, ), cache=True)
def euler_totient(n: int) -> int:
  c, i = n, 1
  while i * i <= n:
    i += 1
    if n % i: continue
    c = c // i * (i - 1)
    while n % i == 0: n //= i
  if n > 1: c = c // n * (n - 1)
  return c