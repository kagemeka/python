from \
  datetime \
import (
  time,
  datetime as dt,
  timedelta as td,
)


  
class TimeConverter:
  

  @staticmethod
  def time_to_sec(
    t: time,
  ) -> int:
    s = t.second
    s += t.minute * 60 
    s += t.hour * 60 ** 2
    return s 

  
  @classmethod
  def time_to_ms(
    cls,
    t: time,
  ) -> int:
    s = cls.time_to_sec(t)
    ms = s * 1000 
    return ms


  @staticmethod
  def time_from_str(
    s: str,
    form: str,
  ) -> time:
    dt_ = dt.strptime(
      s,
      form,
    )
    t = dt_.time()
    return t
  

  @staticmethod 
  def time_from_sec(
    s: int,
  ) -> time:
    td_ = td(seconds=s)
    dt_ = dt.min + td_
    t = dt_.time() 
    return t