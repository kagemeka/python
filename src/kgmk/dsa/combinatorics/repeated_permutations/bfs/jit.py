import numpy as np 
import numba as nb


@nb.njit((nb.i8, nb.i8), cache=True)
def repeated_permutations(n: int, k: int) -> np.ndarray:
  res = np.empty((n ** k, k), np.int64)
  idx_to_add = 0 
  def add_result(a):
    nonlocal idx_to_add
    res[idx_to_add] = a
    idx_to_add += 1
  
  que = [(np.empty(k, np.int64), 0)]
  for a, i in que:
    if i == k:
      add_result(a)
      continue
    for j in range(n):
      b = a.copy()
      b[i] = j
      que.append((b, i + 1))
  return res
     