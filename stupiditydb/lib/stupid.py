"""
Python module to make interaction with stupiditydb easier
"""

import aiohttp
from datetime import datetime as dt


class Review:
    """
    A class containing attributes of a stupiditydb review
    """
    def __init__(self, data):
        self.id: int = data.get("id", 0)
        self.user_id = data["sender"]["discordID"]
        self.stars = data["star"]
        self.comment = data["comment"]
        self.badges = data["sender"]["badges"]
        self.type = data["type"]
        self.timestamp = data["timestamp"]
    
    def datetime(self) -> dt:
        return dt.utcfromtimestamp(self.timestamp)


class ReviewDB:
    def __init__(self, API_BASE: str = "https://manti.vendicated.dev/api"):
        self.API_BASE = API_BASE

    async def api_get(self, endpoint: str, json: bool =True, *args, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.API_BASE + endpoint, *args, **kwargs
            ) as response:
                if json:
                    text = await response.json()
                else:
                    text = await response.text()
        return text

    async def get_user_reviews(self, user_id):
        endpoint = "/reviewdb/users/%s/reviews"
        data: list = await self.api_get(endpoint % user_id)
        if not data["success"]:
            raise Exception("[get_user_reviews] Request returned failure")
        reviews = []
        for review in data["reviews"]:
            reviews.append(Review(review))
        return reviews