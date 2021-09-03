import typing 
import numpy as np 



def solve():
  fw_e: int
  fw_fn: typing.Callable[[int, int], int]
  fw: np.ndarray 


  # TODO cut below

  def fw_get(i):
    nonlocal fw, fw_fn, fw_e
    v = fw_e
    while i > 0:
      v = fw_fn(v, fw[i])
      i -= i & -i
    return v

  def fw_set(i, x):
    nonlocal fw, fw_fn
    while i < len(fw):
      fw[i] = fw_fn(fw[i], x)
      i += i & -i