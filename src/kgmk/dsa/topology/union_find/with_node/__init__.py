import typing
import sys
sys.setrecursionlimit(1 << 20)
import dataclasses



@dataclasses.dataclass 
class Node():
  parent: int
  size: int = 1
  rank: int = 0



class UnionFind():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__a = [Node(i) for i in range(n)]
  

  def find(
    self,
    u: int,
  ) -> int:
    a = self.__a
    pu = a[u].parent
    if pu == u: return u
    pu = self.find(pu)
    a[u].parent = pu
    return pu


  def groups(self) -> typing.List[
    typing.List[int]
  ]:
    n = len(self.__a)
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
    return self.__a[self.find(u)].size


  def unite(
    self,
    u: int,
    v: int,
  ) -> typing.NoReturn:
    u = self.find(u)
    v = self.find(v)
    if u == v: return 
    a = self.__a
    if a[u].size < a[v].size: 
      u, v = v, u
    a[u].size += a[v].size
    a[v].parent = u