import json

import aiohttp
from aiohttp import ContentTypeError

from .auth import Auth


class BaseRequest(Auth):
    async def get(self, version: str = "beta", path=None, args=None, params=None):
        try:
            async with aiohttp.ClientSession() as session:
                token = await self.get_token()
                headers = {"Authorization": f"Bearer {token}"}
                if args is None:
                    url = f"https://api.lexmachina.com/{version}/{path}"
                else:
                    url = f"https://api.lexmachina.com/{version}/{path}/{args}"
                async with session.get(url, headers=headers,
                                       params=params) as response:
                    return await response.json()
        except ContentTypeError:
            return await response.text()

    async def post(self, version: str = "beta", path=None, data=None):
        async with aiohttp.ClientSession() as session:
            token = await self.get_token()
            headers = {"Authorization": f"Bearer {token}"}
            async with session.post(
                    f"https://api.lexmachina.com/{version}/{path}", headers=headers, data=json.dumps(data)
            ) as response:
                return await response.json()
