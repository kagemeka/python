from ...graph import (
  Graph,
  Edge,
)
from ..dijkstra import (
  ShortestDistDijkstra,
)
from ..bellman_ford import (
  ShortestDistBellmanFord,
)


# TODO cut below 

import typing


class ShortestDistJohnson():
  def __call__(
    self,
    g: Graph,
  ) -> typing.List[typing.List[int]]:
    n = g.size
    new_g = Graph.from_size(n + 1)
    for u in range(n):
      for e in g.edges[u]:
        new_g.add_edge(e)

    for i in range(n):
      new_g.add_edge(Edge(n, i, 0)) 
    h = ShortestDistBellmanFord()(new_g, n)[:-1]

    for u in range(n):
      for e in g.edges[u]:
        e.weight += h[u] - h[e.to]

    dist = [None] * n
    dijkstra = ShortestDistDijkstra()
    for i in range(n):
      d = dijkstra(g, i)
      dist[i] = [d[j] - h[i] + h[j] for j in range(n)]  
    return dist