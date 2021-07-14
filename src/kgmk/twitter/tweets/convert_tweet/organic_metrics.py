import dataclasses


@dataclasses.dataclass 
class OrganicMetrics():
  impression_count: int
  url_link_clicks: int
  user_profile_clicks: int
  retweet_count: int
  reply_count: int
  like_count: int
  