from ..prime_numbers.jit import (
  prime_numbers,
)

# TODO cut below
import numpy as np 
import numba as nb 


@nb.njit 
def prime_factor_cnt(n: int) -> np.ndarray:
  pn = prime_numbers(n)
  cnt = np.zeros(n, np.int64)
  for p in pn: cnt[p::p] += 1
  return cnt