# TODO cut below 
import typing
import numba as nb 


S = typing.TypeVar('S')
@nb.njit 
def seg_op(a: S, b: S) -> S: return min(a, b)


@nb.njit 
def seg_e() -> S: return 1 << 60