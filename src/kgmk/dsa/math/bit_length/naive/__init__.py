class BitLength():
  def __call__(self, n: int) -> int:
    l = 0
    while 1 << l <= n: l += 1
    return l