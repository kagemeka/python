from ...graph.pypy import (
  Graph,
)

# TODO cut below

import typing 


class Config():
  def __init__(
    self,
    inf: int = 1 << 60,
  ) -> typing.NoReturn:
    self.inf = inf



class ShortestDistDijkstra():
  def __call__(
    self,
    g: Graph,
    src: int,
  ) -> typing.List[int]:
    import heapq 
    dist = [self.__cfg.inf] * g.size
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


  def __init__(
    self,
    cfg: Config,
  ) -> typing.NoReturn:
    self.__cfg = cfg
    
