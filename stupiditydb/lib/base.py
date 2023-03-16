"""
Python module to hold the base for the two other modules in this folder
"""
import aiohttp


class Base:
    def __init__(self, API_BASE, json=True):
        self.API_BASE = API_BASE
        self.json = json

    async def api_get(
        self,
        endpoint: str,
        method="GET",
        is_json: bool = False,
        return_data: bool = True,
        **kwargs
    ):
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method, self.API_BASE + endpoint, **kwargs
            ) as response:
                if return_data:
                    if self.json or is_json:
                        text = await response.json()
                    else:
                        text = await response.text()
                else:
                    text = response.ok
        return text
