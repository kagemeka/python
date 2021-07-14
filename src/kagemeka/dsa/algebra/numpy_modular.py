import numpy as np



class NumpyModular:


  mod: int = None


  def __init__(
    self,
    mod: int,
  ):
    self.mod = mod 
  

  def mat_pow(
    self,
    a: np.ndarray,
    n: int,
  ) -> np.ndarray:
    if n == 0:
      e = np.identity(
        a.shape[0],
        dtype=np.int64,
      )
      return e 
    x = self.mat_pow(a, n >> 1)
    x = self.mat_dot(x, x)
    if n & 1: 
      x = self.mat_dot(x, a)
    return x
  

  def mat_dot(
    self,
    a: np.ndarray,
    b: np.ndarray,
  ):
    mod = self.mod
    N = 15 
    MASK = (1 << N) - 1
    a0, a1 = a & MASK, a >> N
    b0, b1 = b & MASK, b >> N 
    c0 = np.dot(a0, b0) % mod
    c2 = np.dot(a1, b1) % mod
    c1 = np.dot(
      a0 + a1, 
      b0 + b1,
    ) - c0 - c2
    c1 %= mod
    c = c2 << N * 2
    c += c1 << N
    c += c0
    c %= mod
    return c


  def inv(self, n: int):
    p = self.mod 
    n = int(n)
    return pow(n, p - 2, p)


  def cumprod(self, a):
    l = len(a)
    n = int(np.sqrt(l) + 1)
    a = np.resize(a, (n, n))
    for i in range(n-1):
      a[:, i + 1] *= a[:, i]
      a[:, i + 1] %= self.mod
    for i in range(n-1):
      a[i + 1] *= a[i, -1]
      a[i + 1] %= self.mod
    return np.ravel(a)[:l]

  
  def factorial(self, n: int):
    fact = np.arange(n)
    fact[0] = 1
    return self.cumprod(fact)


  def inv_factorial(
    self, 
    n: int,
  ):
    fact = self.factorial(n)
    ifact = np.arange(1, n + 1)
    ifact[-1] = self.inv(
      fact[-1], 
    )
    return self.cumprod(
      ifact[::-1],
    )[n::-1]