import heapq 
from kgmk.dsa.binary_heap \
import (
  Heap,
)


def test():
  hq = Heap()
  q = []
  for i in range(10, 0, -1):
    hq.push(i)
    heapq.heappush(q, i)
    print(q)
    print(hq)
  while hq:
    print(hq.pop())


if __name__ == '__main__':
  test()