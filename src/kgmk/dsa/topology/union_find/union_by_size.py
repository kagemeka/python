import typing 



class UnionFind():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn: 
    self.__p = list(range(n))
    self.__s = [1] * n
  

  def find(
    self, 
    u: int,
  ) -> int:
    p = self.__p
    if p[u] == u: return u
    p[u] = self.find(p[u])
    return p[u]


  def unite(
    self,
    u: int,
    v: int,
  ) -> typing.NoReturn:
    u = self.find(u)
    v = self.find(v)
    if u == v: return
    p, s = self.__p, self.__s
    if s[u] < s[v]: u, v = v, u
    s[u] += s[v]
    p[v] = u