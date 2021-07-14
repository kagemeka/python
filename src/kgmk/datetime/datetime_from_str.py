from datetime import (
  datetime,
)

class DatetimeFromStr():
  @staticmethod
  def rfc3339_format(
    s: str,
  ) -> datetime:
    f = '%Y-%m-%dT%H:%M:%S.%fZ'
    return datetime.strptime(
      s,
      f,
    )