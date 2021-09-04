from __future__ import annotations 
import typing 
import dataclasses



@dataclasses.dataclass
class SinglyLinkedListNode():
  value: typing.Optional[typing.Any] = None
  next: typing.Optional[SinglyLinkedListNode] = None