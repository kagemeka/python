import numpy as np



class FindDivisors():
  def __call__(self, n: int) -> np.ndarray:
    i = np.arange(int(n ** .5)) + 1
    i = i[n % i == 0]
    return np.unique(np.hstack((i, n // i)))
