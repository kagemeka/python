from ...graph import (
  Graph,
)


# TODO cut below 

import typing 



class ShortestDistDijkstra():
  def __call__(
    self,
    g: Graph,
    src: int,
  ) -> typing.List[int]:
    import heapq 
    inf = float('inf')
    dist = [inf] * g.size
    dist[src] = 0
    hq = [(0, src)]
    while hq:
      du, u = heapq.heappop(hq)
      if du > dist[u]: continue
      for e in g.edges[u]:
        v, dv = e.to, du + e.weight
        if dv >= dist[v]: continue
        dist[v] = dv 
        heapq.heappush(hq, (dv, v))
    return dist


