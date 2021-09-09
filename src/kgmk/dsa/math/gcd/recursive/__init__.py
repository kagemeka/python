class GCD():
  def __call__(self, a: int, b: int) -> int:
    return self(b, a % b) if b else a 

