import typing 
import numpy as np 
import sys 
import numba as nb 


@nb.njit
def sa_doubling(
  a: np.array,
) -> np.array:
  n = a.size
  a = np.searchsorted(
    np.unique(a),
    a,
  )
  cnt = np.zeros(n + 1, dtype=np.int32)
  
  def count_sort(a):
    for x in a: cnt[x + 1] += 1
    for i in range(n): cnt[i + 1] += cnt[i]
    idx = np.empty(n, dtype=np.int32)
    for i in range(n):
      x = a[i]
      idx[cnt[x]] = i
      cnt[x] += 1
    cnt[:] = 0
    return idx 

  k = 1
  rank = a 
  while 1:
    b = np.zeros(n, dtype=np.int64)
    for i in range(n - k):
      b[i] = rank[i + k] + 1
    ord_b = count_sort(b)
    a = rank[ord_b]
    ord_a = count_sort(a)
    sa = ord_b[ord_a]
    c = a[ord_a] << 30 | b[sa]
    rank = np.empty(n, dtype=np.int64)
    rank[sa[0]] = 0
    for i in range(n - 1):
      rank[sa[i + 1]] = rank[sa[i]] + (c[i + 1] > c[i])
    k *= 2
    if k >= n: break
  return sa