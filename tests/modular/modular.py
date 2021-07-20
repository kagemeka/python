'''TODO
pip install -e .[dsa]
'''

from \
  kgmk.dsa.algebra.modular \
  .mod_factory \
import (
  ModFactory,
)
from \
  kgmk.dsa.algebra.modular \
  .factorial \
import (
  ModFactorial,
)


def test():
  mod = 10 ** 9 + 7
  mint = ModFactory(mod)
  a = mint(-1)
  print(a)
  b = mint(-3)
  a += b
  print(a)
  c = 1
  c += a
  print(c)
  c -= a
  print(c)
  d = 1 - a
  print(d)
  e = d 
  e += 1
  print(e, d)
  print(mint(2) ** -1)
  print(2 ** b)

  fn = ModFactorial(mod)
  # fact = fn(1 << 20)
  inv = fn.inv(1 << 21)
  


if __name__ == '__main__':
  test()