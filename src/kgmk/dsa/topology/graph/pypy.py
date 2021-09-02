import typing 


class Node(): ...



class Edge():
  def __init__(
    self,
    from_: int,
    to: int,
    weight: typing.Optional[int] = None,
    capacity: typing.Optional[int] = None,
  ) -> typing.NoReturn:
    self.from_ = from_
    self.to = to
    self.weight = weight 
    self.capacity = capacity




class Graph():
  def __init__(
    self,
    nodes: typing.List[Node],
    edges: typing.List[typing.List[Edge]],
  ) -> typing.NoReturn:
    self.nodes = nodes 
    self.edges = edges 


  @classmethod  
  def from_size(
    cls,
    n: int,
  ) -> typing.Any:
    nodes = [Node() for _ in range(n)]
    edges = [[] for _ in range(n)]
    return cls(nodes, edges)


  def add_edge(
    self,
    e: Edge,
  ) -> typing.NoReturn:
    self.edges[e.from_].append(e)
    

  def add_edges(
    self,
    edges: typing.List[Edge],
  ) -> typing.NoReturn:
    for e in edges:
      self.add_edge(e)
  

  @property
  def size(self) -> int:
    return len(self.nodes)
    
    