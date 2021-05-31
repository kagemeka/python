class DisjointSet: # UnionFind
  def __init__(
    self, 
    n: int,
  ):
    self.parent = list(
      range(n)
    )
    self.rank = [0] * n 
    self.size = [1] * n 


  def find(self, u):
    if self.parent[u] == u: 
      return u
    self.parent[u] = self.find(
      self.parent[u]
    )
    return self.parent[u]


  def unite(self, u, v):
    u = self.find(u)
    v = self.find(v)
    if u == v: return 
    if (
      self.rank[u]
      < self.rank[v]
    ):
      u, v = v, u
    self.parent[v] = u 
    self.size[u] += (
      self.size[v]
    )
    self.rank[u] = max(
      self.rank[u], 
      self.rank[v] + 1,
    )

  
  def same(self, u, v): 
    return (
      self.find(u)
      == self.find(v)
    )


  def groups(
    self, 
    empty_ok=True,
  ):
    n = len(self.rank)
    groups = [
      [] 
      for _ in range(n)
    ]
    for u in range(n): 
      groups[
        self.find(u)
      ].append(u)
    if not empty_ok:
      groups = [
        g 
        for g in groups 
        if g
      ]
    return groups