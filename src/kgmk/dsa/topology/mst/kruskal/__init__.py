from .. import (
  Graph,
  DisjointSet as UnionFind,
)

class Kruskal():

  def __init__(
    self,
  ):
    self._sorted_edges = None


  @property
  def sorted_edges(self):
    if (
      self._sorted_edges
      is not None
    ):
      return (
        self._sorted_edges
      )

    n = len(self.nodes)
    edges = sorted(
      [
        (u, v, e.weight) 
        for u in range(n) 
        for v, e in (
          self.edges[u].items()
        )
      ], 
      key=lambda x: x[2],
    )
    self._sorted_edges = edges 
    return edges

  
  
  def __call__(self):
    n = len(self.nodes)
    uf = UnionFind(n)
    edges = self.sorted_edges
    g = self.__class__(n)
    d = 0
    for u, v, w in edges:
      if uf.same(u, v):
        continue
      uf.unite(u, v)
      g.add_edge(
        u, 
        v, 
        weight=w,
      )
      d += w
    
    return g, d

  

  @property
  def dist(self):
    ...

  

  