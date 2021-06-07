from . import (
  MinimamSpanningTree,
)

from .. import (
  Graph,
  DisjointSet as UnionFind,
)


class BoruvkaMST(
  MinimamSpanningTree,
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


  def __call__(self):  
    n = len(self.nodes)
    uf = UnionFind(n)
    g = self.__class__(n)
    d = 0

    def dfs(u):
      if visited[u]: 
        return (
          inf, 
          (None, None),
        ) 
      visited[u] = True
      cand = []
      for v, e in (
        self.edges[u].items()
      ):
        if uf.same(u, v): 
          cand.append(dfs(v))
          continue 
        cand.append(
          (e.weight, (u, v)),
        )
      return sorted(cand)[0]
    
    while (
      len(set(uf.parent)) !=1 
    ):
      edges = []
      visited = [False] * n
      for u in range(n):
        if visited[u]: 
          continue
        edges.append(dfs(u))
      for w, (u, v) in edges:
        if uf.same(u,v):
          continue
        g.add_edge(
          u, v, weight=w,
        )
        uf.unite(u,v)
        d += w  
      for u in range(n): 
        uf.find(u)

    return g, d