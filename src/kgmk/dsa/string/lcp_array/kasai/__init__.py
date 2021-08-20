import typing



class LCPKasai():
  def __call__(
    self,
    a: typing.List[int],
    sa: typing.List[int],
  ) -> typing.List[int]:
    n = len(a)
    assert n > 0 and len(sa) == n
    rank = [-1] * n
    for i, x in enumerate(sa): rank[x] = i
    h, l = [0] * (n - 1), 0 
    for i in range(n):
      if l > 0: l -= 1
      r = rank[i]
      if r == n - 1: continue
      j = sa[r + 1]
      while i + l < n and j + l < n:
        if a[i + l] != a[j + l]: break
        l += 1
      h[r] = l
    return h