from ...graph import (
  Graph,
)

# TODO cut below

import typing 


class ShortestDistBellmanFord():
  def __call__(self, g: Graph, src: int) -> typing.List[int]:
    n = g.size
    inf = float('inf')
    dist = [inf] * n
    dist[src] = 0
    for _ in range(n - 1):
      for u in range(n):
        for e in g.edges[u]:
          v = e.to
          dist[v] = min(dist[v], dist[u] + e.weight)
    for u in range(n):
      for e in g.edges[u]:
        v = e.to
        if dist[u] + e.weight >= dist[e.to]: continue
        raise Exception('Negative cycle found.')
    return dist