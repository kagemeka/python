from ....graph import (
  Graph,
  Edge,
)

from ....union_find.parent_size_at_same import (
  UnionFind,
)

# TODO cut below 


class MSTKruskal():
  def __call__(
    self,
    g: Graph,
  ) -> Graph:
    n = g.size 
    new_g = Graph.from_size(n)
    edges = [
      (e.weight, u, e.to)
      for u in range(n)
      for e in g.edges[u]
    ]
    edges.sort()
    uf = UnionFind(n)
    for w, u, v in edges:
      if uf.same(u, v): continue
      new_g.add_edge(Edge(u, v, w))
      uf.unite(u, v)    
    return new_g 

  