from ...graph import (
  Graph,
)


# TODO cut below 

import typing 


class ShortestDistDesopoPape():
  def __call__(
    self,
    g: Graph,
    src: int,
  ) -> typing.List[int]:
    import collections 
    inf = float('inf')
    n = g.size 
    dist = [inf] * n
    dist[src] = 0
    dq = collections.deque([src])
    state = [-1] * n
    while dq:
      u = dq.popleft()
      state[u] = 0
      for e in g.edges[u]:
        v, dv = e.to, dist[u] + e.weight 
        if dv >= dist[v]: continue
        dist[v] = dv
        if state[v] == 1: continue 
        if state[v] == -1: dq.append(v)
        else: dq.appendleft(v)
        state[v] = 1
    return dist