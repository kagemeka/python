import typing
import numba as nb
import numpy as np


@nb.njit
def factorize(
  n: int,
  prime_numbers: np.array,
) -> typing.Tuple[
  typing.List[int],
  typing.List[int],
]:
  prime = []
  cnt = []
  for p in prime_numbers:
    if n < 2: return prime, cnt
    if p * p > n: break
    if n % p != 0: continue 
    prime.append(p)
    cnt.append(1)
    n //= p
    while n % p == 0:
      cnt[-1] += 1
      n //= p
  prime.append(n)
  cnt.append(1)
  return prime, cnt


@nb.njit
def factorize_factorial(
  n: int,
  prime_numbers: np.array,
) -> typing.Tuple[
  typing.List[int],
  typing.List[int],
]:
  pn = prime_numbers
  prime = []
  cnt = []
  i = [-1] * len(pn)
  for x in range(n + 1):
    p, c = factorize(x, pn)
    for p, c in zip(p, c):
      if i[p] != -1:
        cnt[i[p]] += c
        continue
      i[p] = len(prime)
      prime.append(p)
      cnt.append(c)
  return prime, cnt