import numpy as np
import numba as nb



@nb.njit
def prime_factorize(
  n: int,
  lpf: np.array,
) -> np.array:
  p, c = [-1], [-1]
  while n > 1:
    i = lpf[n]
    n //= i
    if p[-1] == i:
      c[-1] += 1
      continue
    p.append(i)
    c.append(1)
  return np.vstack((
    np.array(p),
    np.array(c),
  )).T[1:]


@nb.njit
def prime_factorize_factorial(
  n: int,
  lpf: np.array,
) -> np.array:
  prime, cnt = [], []
  idx = np.full(n + 1, -1, dtype=np.int64)
  for i in range(n + 1):
    for p, c in prime_factorize(i, lpf):
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