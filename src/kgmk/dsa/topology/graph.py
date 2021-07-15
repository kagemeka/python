import typing
from typing import (
  List,
  Optional,
)
import dataclasses



@dataclasses.dataclass
class Node:
  id_: Optional[int] = None



@dataclasses.dataclass 
class Edge:
  id_: Optional[int] = None
  from_ : int = ... 
  to: int = ... 
  weight: int = 1
  capacity: int = 0



@dataclasses.dataclass
class Graph:
  nodes: List[Node]
  edges: List[List[Edge]]


  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
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
  ) -> typing.NoReturn:
    i = e.from_ 
    self.edges[i].append(e)
  

  def add_edges(
    self,
    edges: typing.List[Edge],
  ) -> typing.NoReturn:
    for e in edges:
      self.add_edge(e)
  

  @property 
  def size(
    self,
  ) -> int:
    return len(self.nodes)

