

class NormalizeJa():
  def __call__(
    self,
    s: str,
  ) -> str:
    from unicodedata import (
      normalize,
    )
    s = ' '.join(s.split())
    return normalize('NFKC', s)

