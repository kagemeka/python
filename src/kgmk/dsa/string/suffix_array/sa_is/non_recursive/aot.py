import typing
import numpy as np



def sa_is(
  a: np.ndarray,
) -> np.ndarray:
  def _compute_next_array(a, sa, is_lms):
    n = a.size
    lms_idx = sa[is_lms[sa]]
    l = lms_idx.size
    na = np.full(n, -1, dtype=np.int64)
    na[-1] = i = 0
    for j in range(l - 1):
      j, k = lms_idx[j], lms_idx[j + 1]
      for d in range(n):
        j_is_lms = is_lms[j + d]
        k_is_lms = is_lms[k + d]
        if a[j + d] != a[k + d] or j_is_lms ^ k_is_lms: 
          i += 1; break
        if d > 0 and j_is_lms | k_is_lms: break
      na[k] = i
    na = na[na >= 0]
    return na

  def _induce(a, is_s, lms, bucket):
    n, m = a.size, bucket.size
    sa = np.full(n, -1, np.int32)
    
    def _set_lms():
      sa_idx = bucket.cumsum()
      for i in lms[::-1]:
        x = a[i] 
        sa_idx[x] -= 1
        sa[sa_idx[x]] = i
    
    def _induce_l():
      sa_idx = bucket.copy()
      s = 0 
      for i in range(m):
        s, sa_idx[i] = s + sa_idx[i], s
      for i in range(n):
        i = sa[i] - 1
        if i < 0 or is_s[i]: continue
        x = a[i]
        sa[sa_idx[x]] = i
        sa_idx[x] += 1

    def _induce_s():
      sa_idx = bucket.cumsum()
      for i in range(n - 1, -1, -1):
        i = sa[i] - 1
        if i < 0 or not is_s[i]: continue
        x = a[i] 
        sa_idx[x] -= 1
        sa[sa_idx[x]] = i
    
    _set_lms()
    _induce_l()
    _induce_s()
    return sa
    
  def _preprocess(a):
    
    n = a.size
    is_s = np.ones(n, np.bool8)
    for i in range(n - 1, 0, -1):
      is_s[i - 1] = (
        is_s[i] if a[i - 1] == a[i] else
        a[i - 1] < a[i]
      )
    is_lms = np.zeros(n, np.bool8)
    is_lms[np.arange(1, n)[~is_s[:-1] & is_s[1:]]] = True
    lms = np.flatnonzero(is_lms)
    bucket = np.bincount(a)
    return is_s, is_lms, lms, bucket

  if a.min() <= 0: a += 1
  assert (a > 0).all()
  a = np.hstack((a, np.array([0])))

  st: typing.List[typing.Tuple[np.ndarray]] = []
  while True:
    is_s, is_lms, lms, b = _preprocess(a)
    sa = _induce(a, is_s, lms, b)
    st.append((a, is_s, lms, b))
    a = _compute_next_array(a, sa, is_lms)
    l = lms.size
    if a.max() < l - 1: continue
    lms_order = np.empty(l, np.int32)
    for i in range(l): lms_order[a[i]] = i
    break

  while st:
    a, is_s, lms, b = st.pop()
    lms = lms[lms_order]
    lms_order = _induce(a, is_s, lms, b)

  return lms_order[1:]