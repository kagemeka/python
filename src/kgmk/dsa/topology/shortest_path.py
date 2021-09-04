from . import Graph
from abc import abstractmethod



class AStar(ShortestPath):
  def astar(self, src, tgt, heuristic_func):
    cost = [inf] * self.__N
    q = [(heuristic_func(src, tgt), 0, src)]
    while q:
      _, c, u = heappop(q)
      if u == tgt: return c
      if cost[u] != inf: continue 
      cost[u] = c
      for v, e in self.edges[u].items():
        if cost[v] != inf: continue
        h = heuristic_func(v, tgt)
        nc = c + e.weight
        heappush(q, (h+nc, nc, v))        
    return inf
  


class ZeroOneBFS(ShortestPath):
  def bfs01(self, src=0):
    d = [inf]*self.__N
		d[src] = 0
    q = deque([src])
    while q:
      u = q.popleft()
      for v, e in (
        self.edges[u]
        .items()
			):
        dv = d[u] + e.weight
        if d[v] <= dv: continue 
        d[v] = dv
        if e.weight: q.append(v)
        else: q.appendleft(v)
    return d 