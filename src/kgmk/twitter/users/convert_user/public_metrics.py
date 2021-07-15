import dataclasses


@dataclasses.dataclass
class PublicMetrics():
  followers_count: int
  following_count: int
  tweet_count: int
  listed_count: int