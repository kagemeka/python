from . import Graph
from abc import abstractmethod

class ShortestPath(Graph):
  # @abstractmethod
  # def shortest_dist(self, **kwargs):
  #   ...
  ...



  
    
class Dijkstra(ShortestPath):


  def prepare(
      self,
      inf=float('inf'),
      source: int=...,
      **kwargs):

    n = len(self.nodes)
    valid = type(source)==int \
      and 0 <= source < n
    assert valid, 'Invalid source'
    self.dist = [inf] * n
    self.dist[source] = 0
    self.prev = [None] * n
    self.que = [(0, source)]
    self.path_cnt = [0] * n 
    self.path_cnt[source] = 1


  def _search(
        self, u):

    # if path_true: 
    for v, e in \
        self.edges[u].items():
      dv = self.dist[u] = e.weight 
      if dv >= self.dist[v]:
        continue 
      


  def search(self, **kwargs):
    ...
    
  
  def shortest_dist(
      self, **kwargs):
    from heapq import (
      heappush,
      heappop,
    )

    self.prepare(**kwargs)

    # def _search(self, u):

    while self.que:
      du, u = heappop(self.que)
      if self.dist[u] < du: continue
      # self.search 
      for v, e in \
          self.edges[u].items():
        dv = du + e.weight
        if dv >= self.dist[v]:
          continue
        self.dist[v] = dv 
        heappush(self.que, (dv, v))
    return self.dist

  
  def shortest_path_cnt(
      self,
      mod=None):
    from heapq import (
      heappush, 
      heappop,
    )
    
    
    ...
    
    def dijkstra(
        self, 
        src, 
        paths_cnt=False, 
        mod=None):
      dist = [inf] * self.__N; 
      dist[src] = 0
      visited = [False] * self.__N
      paths = [0] * self.__N
      paths[src] = 1
      q = [(0, src)]
      while q:
        d, u = heappop(q)
        if visited[u]: continue
        visited[u] = True
        for v, e in \
          self.edges[u].items():
          dv = d + e.weight
          if dv > dist[v]: continue
          elif dv == dist[v]:
            paths[v] += paths[u]
            if mod: paths[v] %= mod
            continue 
          paths[v], dist[v] = paths[u], dv
          heappush(q, (dv, v))
      if paths_cnt: return dist, paths 
      else: return dist


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
  


class BellmanFord(
    ShortestPath):

  def bellman_ford(self, src):
    n = self.__N
    d = [inf] * n; d[src] = 0
    for _ in range(n-1): 
      for u in range(n):
        for v, e in self.edges[u].items(): d[v] = min(d[v], d[u]+e.weight)
    for u in range(n):
      for v, e in self.edges[u].items():
        if d[u]+e.weight < d[v]: raise Exception('found negative cycle.')
    return d 


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