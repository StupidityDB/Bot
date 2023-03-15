"""
Python module to hold the base for the two other modules in this folder
"""
import aiohttp

class Base:
    def __init__(self, API_BASE):
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