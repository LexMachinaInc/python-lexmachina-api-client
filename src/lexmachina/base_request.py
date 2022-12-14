import json

import aiohttp
from aiohttp import ContentTypeError

from .auth import Auth


class BaseRequest(Auth):
    async def get(self, version: str = "beta", path=None, args=None, params=None):
        try:
            async with aiohttp.ClientSession() as session:
                token = await self.get_token()
                headers = {"Authorization": f"Bearer {token}", "User-Agent": "lexmachina-0.0.1"}
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
            headers = {"Authorization": f"Bearer {token}", "User-Agent": "lexmachina-0.0.1"}
            url = f"https://api.lexmachina.com/{version}/{path}"
            try:

                async with session.post(
                    url, headers=headers, json=data
                ) as response:
                    return await response.json()
            except ContentTypeError:
                return await response.text()
