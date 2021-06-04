from __future__ import (
  annotations,
)

import sys 

from .. import (
  Input,
)

from typing import (
  List,
  NoReturn,
)


class Reader:
  def __init__(
    self,
    src: Input=(
      sys.stdin.buffer
    ),
  ):
    self.src = src


  def __enter__(
    self,
  ) -> Reader:
    src_is_path = False
    src = self.src 
    if type(src) in (
      str, bytes, int,
    ):
      src_is_path = True
      src = open(
        src, 
        mode='r',
      )
    self.src = src 
    self.src_is_path = (
      src_is_path
    )
    return self


  def __exit__(
    self,
    exc_type,
    exc_value,
    traceback,
  ) -> NoReturn:
    if self.src_is_path:
      self.src.close()


  def line(
    self,
  ) -> bytes:
    src = self.src
    l = src.readline()
    return l.rstrip()


  def int_(
    self,
  ) -> int:
    l = self.line()
    return int(l)


  def str_(
    self,
  ) -> str:
    l = self.line()
    return l.decode()


  def line_ints(
    self,
  ) -> List[int]:
    *ints, = map(
      int, 
      self.line().split(),
    )
    return ints

  
  def line_strs(
    self,
  ) -> List[str]:
    return self.str_().split()


  def lines(
    self,
  ) -> List[bytes]:
    src = self.src
    lines = src.readlines()
    lines = [
      l.rstrip()
      for l in lines
    ]
    return lines
  

  def bulk(
    self,
  ) -> bytes:
    src = self.src 
    return src.read()


  def __call__(
    self,
  ) -> bytes:
    return self.bulk()


  def ints(
    self,
  ) -> List[int]:
    *ints, = map(
      int, 
      self().split(),
    )
    return ints
  

  def strs(
    self,
  ) -> List[str]:
    strs = (
      self()
      .decode()
      .split()
    )
    return strs