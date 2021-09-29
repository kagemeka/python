import typing 
import bisect 


class LIS:
  def __call__(self, a: typing.List[int]) -> typing.List[int]:
    inf = 1 << 60
    lis = [inf] * len(a)
    for x in a: lis[bisect.bisect_left(lis, x)] = x
    return lis[:bisect.bisect_left(lis, inf)]