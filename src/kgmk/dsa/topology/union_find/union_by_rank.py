import typing
import sys
sys.setrecursionlimit(1 << 20)



class UnionFind:
  def __init__(
    self, 
    n: int,
  ):
    self.__p = list(range(n))
    self.__r = [0] * n 
    self.__s = [1] * n 


  def find(
    self, 
    u: int,
  ) -> int:
    p = self.__p
    if p[u] == u: return u
    p[u] = self.find(p[u])
    return p[u]
  

  def groups(self) -> typing.List[
    typing.List[int]
  ]:
    n = len(self.__p)
    g = [[] for _ in range(n)]
    for u in range(n): 
      g[self.find(u)].append(u)
    return [x for x in g if x]

  
  def same(
    self,
    u: int,
    v: int,
  ) -> bool:
    return self.find(u) == self.find(v)


  def size(
    self,
    u: int,
  ) -> int:
    return self.__s[self.find(u)]


  def unite(
    self, 
    u: int,
    v: int,
  ) -> typing.NoReturn:
    u = self.find(u)
    v = self.find(v)
    if u == v: return 
    p, s, r = self.__p, self.__s, self.__r
    if r[u] < r[v]: u, v = v, u
    p[v] = u
    s[u] += s[v]
    r[u] = max(r[u], r[v] + 1)