import typing 



class UnionFind():
  def __init__(self, n: int) -> typing.NoReturn:
    self.__a = [-1] * n
  

  def find(self, u: int) -> int:
    a = self.__a
    if a[u] < 0: return u
    a[u] = self.find(a[u])
    return a[u]


  def groups(self) -> typing.List[typing.List[int]]:
    n = len(self.__a)
    g = [[] for _ in range(n)]
    for u in range(n): 
      g[self.find(u)].append(u)
    return [x for x in g if x]

  
  def same(self, u: int, v: int) -> bool:
    return self.find(u) == self.find(v)


  def size(self, u: int) -> int:
    return -self.__a[self.find(u)]


  def unite(self, u: int, v: int) -> typing.NoReturn:
    u, v = self.find(u), self.find(v)
    if u == v: return 
    a = self.__a
    if a[u] > a[v]: u, v = v, u 
    a[u] += a[v]
    a[v] = u