import numpy as np 
import numba as nb 


@nb.njit 
def bit_length_table(n: int) -> np.ndarray:
  l = np.zeros(n, np.int64)
  for i in range(1, n): l[i] = l[i >> 1] + 1
  return l