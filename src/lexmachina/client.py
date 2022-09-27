import json
from typing import Union
from lexmachina.base_request import BaseRequest


class LexMachinaClient(BaseRequest):
    def __init__(self, config_file_path=None, client_id=None, client_secret=None):
        super().__init__(config_file_path, client_id, client_secret)
        self.config_file_path = config_file_path
        self.client_id = client_id
        self.client_secret = client_secret

    async def get_district_cases(self, cases: str):
        response = await self.get(path='district-cases', args=cases)
        return response

    async def query_district_cases(self, data: dict):
        response = await self.post(path='query-district-cases', data=json.dumps(data))
        return response

    async def get_parties(self, parties: list[str]):
        if isinstance(parties, list):
            response = await self.get(path='parties', params={"partyIds": parties})
            return response
        else:
            response = await self.get(path='parties', args=parties)
            return response

    async def search_parties(self, q: str, page_number: int = 1, page_size: int = 500):
        response = await self.get(path='search-parties', params={"q": q,
                                                                 "pageNumber": page_number,
                                                                 "pageSize": page_size})
        return response

    async def get_attorneys(self, attorneys: list[str]):
        if isinstance(attorneys, list):
            response = await self.get(path='attorneys', params={"attorneyIds": attorneys})
            return response
        else:
            response = await self.get(path='attorneys', args=attorneys)
            return response

    async def search_attorneys(self, q: str, page_number: int = 1, page_size: int = 500):
        response = await self.get(path='search-attorneys', params={"q": q,
                                                                   "pageNumber": page_number,
                                                                   "pageSize": page_size})
        return response

    async def get_law_firms(self, law_firms: list[str]):
        if isinstance(law_firms, list):
            response = await self.get(path='law-firms', params={"lawFirmIds": law_firms})
            return response
        else:
            response = await self.get(path='law-firms', args=law_firms)
            return response

    async def search_law_firms(self, q: str, page_number: int = 1, page_size: int = 500):
        response = await self.get(path='search-law-firms', params={"q": q,
                                                                   "pageNumber": page_number,
                                                                   "pageSize": page_size})
        return response

    async def get_federal_judges(self, federal_judges: list[str]):
        if isinstance(federal_judges, list):
            response = await self.get(path='federal-judges', params={"judgeIds": federal_judges})
            return response
        else:
            response = await self.get(path='federal-judges', args=federal_judges)
            return response

    async def get_magistrate_judges(self, magistrate_judges: str):
        response = await self.get(path='magistrate-judges', args=magistrate_judges)
        return response

    async def search_judges(self, q: str):
        response = await self.search(path='search-judges', q=q)
        return response

    async def get_patents(self, patents: list[str]):
        if isinstance(patents, list):
            response = await self.get(path='patents', params={"patentNumbers": patents})
            return response
        else:
            response = await self.get(path='patents', args=patents)
            return response

    async def list_case_resolutions(self):
        response = await self.list(path='list-case-resolutions')
        return response

    async def list_case_tags(self):
        response = await self.list(path='list-case-tags')
        return response

    async def list_case_types(self):
        response = await self.list(path='list-case-types')
        return response

    async def list_courts(self):
        response = await self.list(path='list-courts')
        return response

    async def list_damages(self):
        response = await self.list(path='list-damages')
        return response

    async def list_events(self):
        response = await self.list(path='list-events')
        return response

    async def list_judgment_sources(self):
        response = await self.list(path='list-judgment_sources')
        return response

    async def list(self, path):
        response = await self.get(path=path)
        return response
    async def health(self):
        response = await self.get(path="health")
        return response