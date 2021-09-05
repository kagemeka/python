import numpy as np 
import numba as nb



@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def mst_kruskal(
  n: int,
  csgraph: np.ndarray,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  sort_idx = np.argsort(csgraph[:, 2], kind='mergesort')
  csgraph = csgraph[sort_idx]

  edge_indices = np.zeros(m, np.int64)
  j = 0
  def add_edge(i):
    nonlocal edge_indices, j
    edge_indices[j] = i
    j += 1

  group = np.arange(n)
  for i in range(m):
    u, v, _ = csgraph[i]
    if group[u] == group[v]: continue
    add_edge(i)
    k = group[v]
    for v in range(n):
      if group[v] != k: continue
      group[v] = group[u]

  return csgraph[edge_indices[:j]]