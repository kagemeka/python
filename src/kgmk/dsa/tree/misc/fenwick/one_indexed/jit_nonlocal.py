import typing 
import numpy as np 


S = typing.TypeVar('S')


def solve():
  e: typing.Callable[[], S]
  op: typing.Callable[[S, S], S]
  fw: np.ndarray 


  # TODO cut below

  def fw_get(i):
    nonlocal fw, op, e
    i += 1
    v = e()
    while i > 0:
      v = op(v, fw[i])
      i -= i & -i
    return v

  def fw_set(i, x):
    nonlocal fw, op
    i += 1
    while i < len(fw):
      fw[i] = op(fw[i], x)
      i += i & -i