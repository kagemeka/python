import numpy as np 
import numba as nb 


@nb.njit((nb.i8, ), cache=True)
def choose_pascal(n: int) -> np.ndarray:
  choose = np.zeros((n + 1, n + 1), np.int64)
  choose[:, 0] = 1
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      choose[i, j] = choose[i - 1, j] + choose[i - 1, j - 1]
  return choose