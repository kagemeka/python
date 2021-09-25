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