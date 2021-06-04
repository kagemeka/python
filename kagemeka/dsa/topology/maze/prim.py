from . import (
  MinimamSpanningTree,
)

from .. import (
  Graph,
  DisjointSet as UnionFind,
)

from heapq import (
  heappush, 
  heappop,
)



class RandomizedPrimMaze(
  Graph,
):
  def __init__(
    self,
    *args,
    **kwargs,
  ):
    super().__init__(
      *args,
      **kwargs,
    )
  

  def __call__(
    self, 
    src=0,
  ):
    n = len(self.nodes)
    g = self.__class__(n)
    parent, visited, dist = (
      [None] * n, 
      [False] * n, 
      0,
    )
    q = [(0, (src, src))]
    while q:
      d, (w, u) = heappop(q)
      if visited[u]: 
        continue 
      visited[u], parent[u] = (
        True, w,
      ) 
      dist += d
      g.add_edge(
        w, u, weight=d,
      )  
      for v, e in (
        self.edges[u].items()
      ):
        if visited[v]:
          continue
        heappush(
          q, 
          (e.weight, (u, v)),
        )
    return g, dist