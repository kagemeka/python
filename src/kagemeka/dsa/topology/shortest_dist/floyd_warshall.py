from ..graph import (
  Graph,
)


# cut below



class FloydWarshall:
  

  def __init__(
    self,
    graph: Graph,
  ):
    self.g = graph
    self.inf = float('inf') 


  def __call__(
    self,
  ) -> None:
    self.init_dist_mat()
    n = self.g.size 
    for i in range(n):
      self.mid = i 
      self.support0()
  

  def support0(self):
    n = self.g.size
    for i in range(n):
      self.src = i
      self.support1()
    

  def support1(self):
    n = self.g.size 
    dist = self.dist 
    k, i = self.mid, self.src 
    for j in range(n):
      d = min(
        dist[i][j],
        dist[i][k] + dist[k][j]
      )
      dist[i][j] = d
    

  def init_dist_mat(
    self,
  ):
    n = self.g.size
    dist = [
      [self.inf] * n
      for _ in range(n)
    ]
    self.dist = dist 
    for i in range(n):
      self.i = i 
      self.__init_dist()

  
  def __init_dist(
    self,
  ):
    dist = self.dist 
    i = self.i 
    dist[i][i] = 0 
    g = self.g
    for e in g.edges[i]:
      j = e.to
      dist[i][j] = e.weight