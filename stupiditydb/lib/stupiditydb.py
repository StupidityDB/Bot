"""
Python module to make interaction with stupiditydb easier
"""
import config
from lib.base import Base


class StupidityDB(Base):
    def __init__(self, API_BASE: str = "https://manti.vendicated.dev"):
        super().__init__(API_BASE, json=False)

    async def get_user_stupidity(self, user_id):
        endpoint = (
            "/getuser?discordid=%s"  # todo: make this a parameter for api_get instead
        )
        data: list = await self.api_get(endpoint % user_id)
        return data

    async def vote_user(self, user_id: int, sender_user_id: int):
        data = {
            "token": config.token,
            "discordid": str(user_id),
            "senderdiscordid": str(sender_user_id),
        }
        endpoint = "/vote"
        data = await self.api_get(endpoint, method="PUT", json=data)
        return data
