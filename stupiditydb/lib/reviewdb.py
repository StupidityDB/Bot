"""
Python module to make interaction with reviewdb easier
"""

from datetime import datetime as dt

from lib.base import Base


class Review:
    """
    A class containing attributes of a reviewdb review
    """

    def __init__(self, data):
        self.review_id: int = data.get("id", 0)
        self.user_id = data["sender"]["discordID"]
        self.stars = data["star"]
        self.comment = data["comment"]
        self.badges = data["sender"]["badges"]
        self.type = data["type"]
        self.timestamp = data["timestamp"]

    def datetime(self) -> dt:
        return dt.utcfromtimestamp(self.timestamp)


class ReviewDB(Base):
    def __init__(self, API_BASE: str = "https://manti.vendicated.dev/api"):
        super().__init__(API_BASE)

    async def get_user_reviews(self, user_id, include_system=False):
        endpoint = "/reviewdb/users/%s/reviews"
        data: list = await self.api_get(endpoint % user_id)
        if not data["success"]:
            raise Exception("[get_user_reviews] Request returned failure")
        reviews = []
        for review in data["reviews"]:
            if include_system or review["type"] != 3:
                reviews.append(Review(review))
        return reviews