
class Load():
  def __call__(
    self,
    path: str,
  ) -> object:
    import yaml
    with open(
      file=path,
      mode='r',
    ) as stream:
      return yaml.load(
        stream=stream,
        Loader=yaml.FullLoader,
      )