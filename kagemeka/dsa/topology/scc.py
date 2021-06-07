
def scc(self): # strongly connected components
  n = self.__N
  visited, q, root, r = [False]*n, [], [None]*n, 0
  gg = self.__class__(n)
  for u in range(n):
    for v in self.edges[u]: gg.add_edge(v, u)
  
  def dfs(u):
    if visited[u]: return
    visited[u] = True 
    for v in self.edges[u]: dfs(v)
    q.append(u)

  def rev_dfs(u, r):
    if root[u] is not None: return 
    root[u] = r 
    for v in gg.edges[u]: rev_dfs(v, r)

  for u in range(n): dfs(u)
  for u in q[::-1]: rev_dfs(u, r); r += 1
  return root
