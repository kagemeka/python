import typing
import numpy as np
import numba as nb


@nb.njit((nb.i8[:, :], np.i8[:], nb.i8), cache=True)
def euler_tour(
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray]:
  n = g[:, :2].max() + 1
  parent = np.full(n, -1, np.int64)
  depth = np.zeros(n, np.int64)
  tour = np.empty(n * 2, np.int64)
  visited = np.zeros(n, np.bool8)
  st = [root]
  for i in range(2 * n):
    u = st.pop()
    tour[i] = u
    if visited[u]: continue
    visited[u] = True
    st.append(u)
    for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
      if v == parent[u]: continue
      parent[v] = u
      depth[v] = depth[u] + 1
      st.append(v)
  return tour, parent, depth