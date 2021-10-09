import typing
import numpy as np
import numba as nb 



@nb.njit
def sort_csgraph(
  n: int, 
  g: np.ndarray,
) -> typing.Tuple[(np.ndarray, ) * 3]:
  sort_idx = np.argsort(g[:, 0], kind='mergesort')
  g = g[sort_idx]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  original_idx = np.arange(len(g))[sort_idx]
  return g, edge_idx, original_idx 

