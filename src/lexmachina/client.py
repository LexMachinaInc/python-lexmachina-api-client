from .base_request import BaseRequest


class LexMachinaClient(BaseRequest):
    def __init__(self, config_file_path=None, client_id=None, client_secret=None):
        super().__init__(config_file_path, client_id, client_secret)
        self.config_file_path = config_file_path
        self.client_id = client_id
        self.client_secret = client_secret

    async def get_district_cases(self, cases: int):
        response = await self.get(path='district-cases', args=cases)
        return response

    async def query_district_cases(self, data: dict):
        response = await self.post(path='query-district-cases', data=data)
        return response

    async def get_parties(self, parties: list[str]):
        if isinstance(parties, list):
            response = await self.get(path='parties', params={"partyIds": parties})
        else:
            response = await self.get(path='parties', args=parties)
        return response

    async def search_parties(self, q: str, page_number: int = 1, page_size: int = 500):
        response = await self.get(path='search-parties', params={"q": q,
                                                                 "pageNumber": page_number,
                                                                 "pageSize": page_size})
        return response

    async def get_attorneys(self, attorneys: list[int]):
        if isinstance(attorneys, list):
            response = await self.get(path='attorneys', params={"attorneyIds": attorneys})
        else:
            response = await self.get(path='attorneys', args=attorneys)
        return response

    async def search_attorneys(self, q: str, page_number: int = 1, page_size: int = 500):
        response = await self.get(path='search-attorneys', params={"q": q,
                                                                   "pageNumber": page_number,
                                                                   "pageSize": page_size})
        return response

    async def get_law_firms(self, law_firms: list[int]):
        if isinstance(law_firms, list):
            response = await self.get(path='law-firms', params={"lawFirmIds": law_firms})
        else:
            response = await self.get(path='law-firms', args=law_firms)
        return response

    async def search_law_firms(self, q: str, page_number: int = 1, page_size: int = 500):
        response = await self.get(path='search-law-firms', params={"q": q,
                                                                   "pageNumber": page_number,
                                                                   "pageSize": page_size})
        return response

    async def get_federal_judges(self, federal_judges: list[int]):
        if isinstance(federal_judges, list):
            response = await self.get(path='federal-judges', params={"federalJudgeIds": federal_judges})
        else:
            response = await self.get(path='federal-judges', args=federal_judges)
        return response

    async def get_magistrate_judges(self, magistrate_judges: str):
        response = await self.get(path='magistrate-judges', args=magistrate_judges)
        return response

    async def search_judges(self, q: str):
        response = await self.get(path='search-judges', params={"q": q})
        return response

    async def get_patents(self, patents: list[str]):
        if isinstance(patents, list):
            response = await self.get(path='patents', params={"patentNumbers": patents})
        else:
            response = await self.get(path='patents', args=patents)
        return response

    async def list_case_resolutions(self):
        return await self.list(path='list-case-resolutions')

    async def list_case_tags(self):
        return await self.list(path='list-case-tags')

    async def list_case_types(self):
        return await self.list(path='list-case-types')

    async def list_courts(self):
        return await self.list(path='list-courts')

    async def list_damages(self):
        return await self.list(path='list-damages')

    async def list_events(self):
        return await self.list(path='list-events')

    async def list_judgment_sources(self):
        return await self.list(path='list-judgment-sources')

    async def list(self, path):
        response = await self.get(path=path)
        return response

    async def health(self):
        response = await self.get(path="health")
        return response
