from ...graph import (
  Graph,
)


# cut below

import typing 
import dataclasses


@dataclasses.dataclass 
class Config():
  inf: int = 1 << 60



class FloydWarshall():
  def __call__(
    self,
    g: Graph,
  ) -> typing.List[typing.List[int]]:
    n = g.size 
    dist = [[self.__cfg.inf] * n for _ in range(n)]
    for i in range(n): dist[i][i] = 0
    for u in range(n):
      for e in g.edges[u]:
        dist[u][e.to] = min(dist[u][e.to], e.weight)
    
    for k in range(n):
      for i in range(n):
        for j in range(n):
          dist[i][j] = min(
            dist[i][j], 
            dist[i][k] + dist[k][j],
          )
    return dist
    

  def __init__(
    self,
    cfg: Config,
  ) -> typing.NoReturn:
    self.__cfg = cfg 