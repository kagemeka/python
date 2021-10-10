import typing
import numpy as np
import numba as nb 



@nb.njit 
def sort_csgraph(
  n: int, 
  g: np.ndarray,
) -> typing.Tuple[(np.ndarray, ) * 3]:
  idx = g[:, 0] << 31 | g[:, 1]
  sort_idx = np.argsort(idx, kind='mergesort')
  g = g[sort_idx]
  original_idx = np.arange(len(g))[sort_idx]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  return g, edge_idx, original_idx