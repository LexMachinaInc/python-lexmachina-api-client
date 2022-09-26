import json

from lexmachina.base_request import BaseRequest

class LexMachinaClient(BaseRequest):
    def __init__(self, config_file_path=None, client_id=None, client_secret=None):
        super().__init__(config_file_path, client_id, client_secret)
        self.config_file_path = config_file_path
        self.client_id = client_id
        self.client_secret = client_secret

    async def get_district_cases(self, cases):
        response = await self.get(path='/district-cases', args=cases)
        return response

    async def query_district_cases(self, data: dict):
        response = await self.post(path='/query-district-cases', data=json.dumps(data))
        return response



