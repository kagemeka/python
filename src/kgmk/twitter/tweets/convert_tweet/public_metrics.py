import dataclasses


@dataclasses.dataclass
class PublicMetrics():
  like_count: int
  quote_count: int
  reply_count: int
  retweet_count: int