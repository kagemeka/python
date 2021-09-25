import typing



class PrimeFactors():
  def __call__(self, n: int) -> typing.NoReturn:
    a = []
    p = 2
    while p * p <= n:
      if n % p:
        p += 1
        continue
      a.append(p)
      while not n % p: n //= p
    if n > 1: a.append(n)
    return a
