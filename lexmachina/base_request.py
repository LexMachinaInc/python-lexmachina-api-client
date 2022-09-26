import configparser
import json

import aiohttp

from lexmachina.auth import Auth


class BaseRequest(Auth):
    async def get(self, version: str = "beta", path=None, args=None, params=None):
        async with aiohttp.ClientSession() as session:
            token = await self.get_token()
            headers = {"Authorization": f"Bearer {token}"}
            async with session.get(f"https://api.lexmachina.com/{version}/{path}/{args}", headers=headers,
                                   params=params) as response:
                return await response.json()

    async def post(self, version: str = "beta", path=None, data=None):
        async with aiohttp.ClientSession() as session:
            token = await self.get_token()
            headers = {"Authorization": f"Bearer {token}"}
            async with session.post(
                    f"https://api.lexmachina.com/{version}/{path}", headers=headers, data=json.dumps(data)
            ) as response:
                return await response.json()
