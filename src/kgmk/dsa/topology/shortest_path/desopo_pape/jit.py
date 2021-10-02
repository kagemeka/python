import numpy as np
import numba as nb 



@nb.njit(
  (nb.i8, nb.i8[:, :], nb.i8),
  cache=True,
) 
def shortest_dist_desepo_pape(
  n: int,
  csgraph: np.ndarray,
  src: int,
) -> np.ndarray:
  assert csgraph.shape == (len(csgraph), 3)
  inf = 1 << 60
  assert inf > csgraph[:, 2].max() * n
  sort_idx = np.argsort(csgraph[:, 0], kind='mergesort')
  csgraph = csgraph[sort_idx]
  edge_idx = np.searchsorted(csgraph[:, 0], np.arange(n + 1))
  dist = np.full(n, inf, np.int64)
  dist[src] = 0

  dq = np.zeros(1 << 20, np.int64)
  dq_l, dq_r = 0, -1

  def deque_append(x):
    nonlocal dq, dq_r
    dq_r += 1
    dq[dq_r] = x

  def deque_appendleft(x):
    nonlocal dq, dq_l
    dq_l -= 1
    dq[dq_l] = x 
  
  def deque_popleft():
    nonlocal dq, dq_l
    v = dq[dq_l]
    dq_l += 1
    return v

  def deque_empty():
    nonlocal dq_l, dq_r 
    return dq_l == dq_r + 1
  
  deque_append(src)
  state = np.full(n, -1, np.int64)

  while not deque_empty():
    u = deque_popleft()
    state[u] = 0
    for i in range(edge_idx[u], edge_idx[u + 1]):
      _, v, w = csgraph[i]
      dv = dist[u] + w 
      if dv >= dist[v]: continue
      dist[v] = dv
      if state[v] == 1: continue
      if state[v] == -1: deque_append(v)
      else: deque_appendleft(v)
      state[v] = 1      
  return dist