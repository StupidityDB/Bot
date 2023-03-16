"""
Python module to hold the base for the two other modules in this folder
"""
import aiohttp


class Base:
    def __init__(self, API_BASE, json=True):
        self.API_BASE = API_BASE
        self.json = json

    async def api_get(self, endpoint: str, is_json: bool = False, *args, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.API_BASE + endpoint, *args, **kwargs
            ) as response:
                if self.json or is_json:
                    text = await response.json()
                else:
                    text = await response.text()
        return text
