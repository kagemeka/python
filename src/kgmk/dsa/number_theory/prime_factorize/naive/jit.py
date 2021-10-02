import numpy as np
import numba as nb 



@nb.njit
def prime_factorize(
  n: int,
) -> np.array:
  p, c = [], []
  i = 1
  while i * i < n:
    i += 1
    if n % i: continue
    p.append(i)
    c.append(0)
    while n % i == 0:
      n //= i
      c[-1] += 1
  if n > 1: 
    p.append(n)
    c.append(1)
  return np.vstack((
    np.array(p),
    np.array(c),
  )).T


@nb.njit
def prime_factorize_factorial(
  n: int,
) -> np.array:
  prime, cnt = [], []
  idx = np.full(n + 1, -1, dtype=np.int64)
  for i in range(n + 1):
    for p, c in prime_factorize(i):
      i = idx[p]
      if i != -1:
        cnt[i] += c
        continue
      idx[p] = len(prime)
      prime.append(p)
      cnt.append(c)
  return np.vstack((
    np.array(prime),
    np.array(cnt),
  )).T 