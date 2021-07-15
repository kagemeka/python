from datetime import (
  datetime,
)


class DatetimeToRFC3339():
  def __call__(
    self,
    dt: datetime,
  ) -> str:
    return f'{dt.isoformat()}Z'