"""
Python module to make interaction with stupiditydb easier
"""
from lib.base import Base

class StupidityDB(Base):
    def __init__(self, API_BASE: str = "https://manti.vendicated.dev"):
        super().__init__(API_BASE)

    async def get_user_stupidity(self, user_id):
        endpoint = (
            "/getuser?discordid=%s"  # todo: make this a parameter for api_get instead
        )
        data: list = await self.api_get(endpoint % user_id, json=False)
        return data
