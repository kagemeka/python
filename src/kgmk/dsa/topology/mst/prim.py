

from .. import (
  Graph,
  DisjointSet as UnionFind,
)

from heapq import (
  heappush, 
  heappop,
)


class Prim():

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
    return_parent=False,
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
    if return_parent: 
      return g, dist, parent
    return g, dist

    