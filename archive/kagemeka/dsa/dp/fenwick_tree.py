class FenwickTree:


  def __init__(self, n: int):
    self.data = [0] * (n + 1)


  def add(
    self, 
    i: int, 
    x: int,
  ):
    n = len(self.data)
    while i <= n: 
      self.data[i] += x
      i += i & -i


  def _sum(
    self, 
    i: int,
  ):
    s = 0
    while i > 0: 
      s += self.data[i]
      i -= i & -i
    return s


  def sum(
    self, 
    l: int, 
    r: int,
  ):
    assert l >= 1, '1-indexed'
    s = self._sum(r)
    s -= self._sum(l - 1)
    return s