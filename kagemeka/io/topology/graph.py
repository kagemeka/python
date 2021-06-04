from typing import (
  List,
)


from dataclasses import (
  dataclass,
)



@dataclass
class Node:
  id_: int = None



@dataclass
class Edge:
  id_: int = None
  from_ : int = ...
  to: int = ...
  weight: int = 1
  capacity: int = 0



@dataclass
class Graph:


  nodes: List[Node]
  edges: List[List[Edge]]


  def __init__(
    self,
    n: int,
  ):
    nodes = [
      Node(i)
      for i in range(n)
    ]
    edges = [
      [] for _ in range(n)
    ]
    self.nodes = nodes 
    self.edges = edges
  

  def add_edge(
    self,
    e: Edge,
  ):
    i = e.from_ 
    self.edges[i].append(e)
  

  def add_edges(
    self,
    edges: List[Edge],
  ):
    for e in edges:
      self.add_edge(e)
  

  @property 
  def size(self):
    return len(self.nodes)