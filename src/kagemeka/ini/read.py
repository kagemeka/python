from typing import (
  Any,
  Mapping,
)


class Read():
  def __call__(
    self,
    path: str,
  ) -> Mapping[
    str,
    Mapping[str, Any],
  ]:
    from configparser import (
      ConfigParser,
    )
    cp = ConfigParser()
    cp.read(filenames=path)  
    return cp._sections
