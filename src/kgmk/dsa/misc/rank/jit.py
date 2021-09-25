import numpy as np 
import numba as nb 



@nb.njit
def rank(a: np.ndarray) -> np.ndarray:
  return np.argsort(np.argsort(a))


@nb.njit
def reversed_rank(a: np.ndarray) -> np.ndarray:
  return np.argsort(np.argsort(a)[::-1])