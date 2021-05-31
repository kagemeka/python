import numpy as np 



class PrimeNumbers:

  def __init__(
    self, 
    n: int = 1 << 20,
  ) -> None:
    is_prime = self.search(n)
    self._is_prime = is_prime
    self.make_sparse()


  def __iter__(self):
    return iter(self.values)


  def __getitem__(
    self,
    i: int,
  ):
    return self.values[i] 
  

  def __repr__(self):
    return f'{self.values}'
  

  def is_prime(
    self,
    n: int,
  ) -> bool:
    return self._is_prime[n]


  def make_sparse(
    self,
  ) -> None:
    values = np.flatnonzero(
      self._is_prime,
    )
    self.values = values


  @staticmethod
  def search(
    n: int,
  ) -> np.ndarray:
    is_prime = np.ones(n)
    is_prime[:2] = 0
    i = 0 
    while i * i < n:
      i += 1
      if not is_prime[i]:
        continue
      is_prime[i * 2::i] = 0
    return is_prime