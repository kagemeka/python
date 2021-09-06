from ....graph import (
  Graph,
  Edge,
)


class MSTPrim():
  def __call__(
    self,
    g: Graph,
  ) -> Graph:
    import heapq
    n = g.size 
    new_g = Graph.from_size(n)
    visited = [False] * n
    inf = 1 << 60
    weight = [inf] * n
    hq = [(0, -1, 0)]
    while hq:
      wu, pre, u = heapq.heappop(hq)
      if visited[u]: continue
      visited[u] = True
      if pre != -1:
        new_g.add_edge(Edge(pre, u, wu))
      for e in g.edges[u]:
        v, wv = e.to, e.weight
        if visited[v] or wv >= weight[v]: continue
        weight[v] = wv 
        heapq.heappush(hq, (wv, u, v))
    return new_g 