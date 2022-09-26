import aiohttp
import configparser
from os import getcwd
from pathlib import Path
class Auth:
    def __init__(self, config_file_path=None, client_id=None, client_secret=None) -> None:
        self.config_file_path = config_file_path
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = "https://api.lexmachina.com/oauth/client_credential/accesstoken"
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    async def get_token(self):
        config = configparser.ConfigParser()
        if not self.config_file_path:
            config_file = Path("config/config.ini")
        else:
            config_file = Path(self.config_file_path)
        async with aiohttp.ClientSession() as session:
            if self.client_id is None and self.client_secret is None:
                if config_file.is_file():
                    config.read(config_file)
                    async with session.post(self.token_url, headers=self.headers, data={
                        "grant_type": "client_credentials",
                        "client_id": config.get("CREDENTIALS", "CLIENT_ID"),
                        "client_secret": config.get("CREDENTIALS", "CLIENT_SECRET")
                    }) as response:
                        if response.status == 200:
                            return await response.json()
                        else:
                            return {"error": await response.json()}
            else:
                async with session.post(self.token_url, headers=self.headers, data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret
            }) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        return {"error": await response.json()}




    

