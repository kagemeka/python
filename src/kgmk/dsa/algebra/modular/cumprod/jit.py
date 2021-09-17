import typing 
import numpy as np
import numba as nb




@nb.njit((nb.i8[:], nb.i8), cache=True)
def mod_cumprod(a: np.ndarray, mod: int) -> typing.NoReturn:
  for i in range(a.size - 1): a[i + 1] = a[i + 1] * a[i] % mod