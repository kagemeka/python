import numpy as np



class FindDivisors():
  def __call__(
    self,
    n: int,
  ) -> np.array:
    i = np.arange(int(n ** .5))
    i += 1
    i = i[n % i == 0]
    i = np.hstack((i, n // i))
    return np.unique(i)