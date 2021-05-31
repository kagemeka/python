from typing import (
  List,
)


from typing import (
  Tuple,
)


import numpy as np



class IntExt:
  

  @staticmethod
  def bit_count(
    n: int,
  ) -> int:
    cnt = 0
    l = n.bit_length()
    for _ in range(l): 
      cnt += n & 1 
      n >>= 1 
    return cnt
  

  @staticmethod 
  def divisors(
    n: int,
  ) -> List[int]:
    divs = []
    i = 0
    while i * i <= n:
      i += 1
      if n % i: continue 
      divs.append(i)
      j = n // i 
      if j == i: continue 
      divs.append(j)
    divs.sort()
    return divs


  @classmethod
  def gcd(
    cls,
    a: int,
    b: int,
  ) -> int:
    if b == 0:
      return abs(a)
    return cls.gcd(b, a % b)


  @classmethod
  def lcm(
    cls,
    a: int,
    b: int,
  ) -> int:
    return abs(
      a // cls.gcd(a, b) * b,
    )


  @classmethod
  def egcd(
    cls,
    a: int,
    b: int,
  ) -> Tuple[int, ...]:
    if b == 0:
      return abs(a), 1, 0
    q, r = divmod(a, b)
    g, y, x = cls.egcd(b, r)
    y -= q * x 
    return g, x, y