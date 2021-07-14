import dataclasses


@dataclasses.dataclass
class NonPublicMetrics():
  impression_count: int
  url_link_clicks: int
  user_profile_clicks: int
  