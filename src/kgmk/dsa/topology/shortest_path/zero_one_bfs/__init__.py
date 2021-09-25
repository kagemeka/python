


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