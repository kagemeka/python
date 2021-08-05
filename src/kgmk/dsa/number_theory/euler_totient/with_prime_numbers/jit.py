import numpy as np
import numba as nb



@nb.njit
def euler_totient(
  n: int,
  prime_numbers: np.array,
) -> int:
  c = n
  for p in prime_numbers:
    if p * p > n: break
    if n % p: continue
    c = c // p * (p - 1)
    while not n % p: n //= p
  if n > 1:
    c = c // n * (n - 1)
  return c