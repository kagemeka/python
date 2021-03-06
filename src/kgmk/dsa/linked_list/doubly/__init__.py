from __future__ import annotations 
import typing 
import dataclasses



@dataclasses.dataclass
class DoublyLinkedListNode():
  value: typing.Optional[typing.Any] = None
  left: typing.Optional[DoublyLinkedListNode] = None
  right: typing.Optional[DoublyLinkedListNode] = None
