from kgmk.dsa.linked_list.doubly import (
  DoublyLinkedList,
  DoublyLinkedListNode,
)

# TODO cut below

import typing


class Deque():
  def __bool__(self) -> bool:
    a = self.__a 
    return a.first is not None


  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__a = DoublyLinkedList()


  def append(
    self,
    v: typing.Any,
  ) -> typing.NoReturn:
    a = self.__a
    x = DoublyLinkedListNode(value=v, left=a.last)
    if x.left is None:
      a.first = x 
    else:
      a.last.right = x 
    a.last = x 
  

  def appendleft(
    self,
    v: typing.Any,
  ) -> typing.NoReturn:
    a = self.__a
    x = DoublyLinkedListNode(value=v, right=a.first)
    if x.right is None:
      a.last = x 
    else:
      a.first.left = x
    a.first = x 
  

  def pop(
    self,
  ) -> typing.Any:
    a = self.__a
    if a.last is None:
      raise Exception('cannot pop from empty deque.')
    v = a.last.value
    a.last = a.last.left
    if a.last is None:
      a.first = None 
    else:
      a.last.right = None 
    a.last.right = None
    return v 
    

  def popleft(
    self,
  ) -> typing.Any:
    a = self.__a
    if a.first is None:
      raise Exception('cannot pop from empty deque.')
    v = a.first.value
    a.first = a.first.right
    if a.first is None:
      a.last = None
    else:
      a.first.left = None
    return v