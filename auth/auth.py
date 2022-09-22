import requests
import asyncio
import aiohttp

class Auth:
    def __init__(self, client_id, client_secret) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = "https://api.lexmachina.com/oauth/client_credential/accesstoken"
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    async def get_token(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(self.token_url, headers=self.headers, data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret
                }) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {"error" : await response.json()}

    

