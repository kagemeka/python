class EulerTotient():
  def __call__(
    self,
    n: int,
  ) -> int:
    c = n
    p = 2
    while p * p <= n:
      if n % p:
        p += 1 
        continue
      c = c // p * (p - 1)
      while not n % p: n //= p
    if n > 1: 
      c = c // n * (n - 1)
    return c