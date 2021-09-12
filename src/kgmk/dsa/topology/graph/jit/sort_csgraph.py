import typing
import numpy as np
import numba as nb 



@nb.njit((nb.i8, nb.i8[:, :], ), cache=True)
def sort_csgraph(
  n: int, 
  csgraph: np.ndarray,
) -> typing.Tuple[
  np.ndarray,
  np.ndarray,
  np.ndarray,
]:
  sort_idx = np.argsort(csgraph[:, 0], kind='mergesort')
  csgraph = csgraph[sort_idx]
  edge_idx = np.searchsorted(csgraph[:, 0], np.arange(n + 1))
  original_idx = np.arange(len(csgraph))[sort_idx]
  return csgraph, edge_idx, original_idx