import re



class ChangePathIgnoreCase():
  def __call__(
    s: str,
    ptn: str,
    to: str,
  ) -> str:
    return re.sub(
      pattern=ptn,
      repl=to,
      string=s,
      flags=re.IGNORECASE,
    )
  