class GCD():
  def __call__(self, a: int, b: int) -> int:
    while b: a, b = b, a % b
    return a 
