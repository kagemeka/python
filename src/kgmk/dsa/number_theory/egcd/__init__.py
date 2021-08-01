import typing


def egcd(
  a: int,
  b: int,
) -> typing.Tuple[int, ...]:
  if b == 0:
    return abs(a), 1, 0
  q, r = divmod(a, b)
  g, y, x = egcd(b, r)
  y -= q * x 
  return g, x, y