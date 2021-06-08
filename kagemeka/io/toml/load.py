class Load():
  def __call__(
    self,
    path: str,
  ) -> dict:
    import toml
    with open(
      file=path,
      mode='r',
    ) as f:
      return toml.load(
        f=f,
      )