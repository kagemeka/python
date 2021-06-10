from .tree import (
  Tree,
)


# cut below


from typing import (
  List,
)


from collections import (
  deque,
)



class TreeBFS:

  root: int
  depth: int
  dist: int
  parent: List[int]


  def __init__(
    self,
    tree: Tree,
  ):
    self.g = tree 
    self.inf = float('inf')


  def search(
    self,
    root: int,
  ):
    self.src = root
    self.init_parent()
    self.init_depth()
    self.init_dist()
    self.set_queue()
    que = self.queue 
    que.append(root)
    while que:
      x = que.popleft()
      self.explore(x)
  

  def explore(
    self,
    u: int,
  ):
    g = self.g
    dep = self.depth 
    dist = self.dist 
    par = self.parent
    que = self.queue
    for e in g.edges[u]:
      v = e.to
      if dep[v] is not None:
        continue 
      d = e.weight
      dep[v] = dep[u] + 1
      dist[v] = dist[u] + d
      par[v] = u
      que.append(v)


  def set_queue(self):
    que = deque()
    self.queue = que


  def init_depth(self):
    dep = [None] * self.g.size
    dep[self.src] = 0
    self.depth = dep


  def init_parent(self):
    par = [None] * self.g.size
    par[self.src] = self.src
    self.parent = par


  def init_dist(self):
    inf = self.inf 
    dist = [inf] * self.g.size
    dist[self.src] = 0
    self.dist = dist 