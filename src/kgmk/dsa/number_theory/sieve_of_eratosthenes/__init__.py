import typing



class SieveOfEratosthenes():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> typing.Tuple[int]:
    s = [True] * n
    s[0] = s[1] = False
    i = 0 
    while i * i < n:
      i += 1
      if not s[i]: continue
      for j in range(
        i * 2,
        n,
        i,
      ): s[j] = False
    return tuple(s)