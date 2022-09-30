import pytest

from src.lexmachina.client import LexMachinaClient


class TestGetDistrictCase:
    client = LexMachinaClient("config.ini")


    @pytest.mark.asyncio
    @pytest.mark.parametrize("cases", [0, -2, 999999999])
    async def test_get_district_case_integer_fuzz(self, cases):

        response = await self.client.get_district_cases(cases=cases)
        assert response.get("detail") == "case_id not found"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("cases", [66])
    async def test_get_district_case_positive(self, cases):
        response = await self.client.get_district_cases(cases=cases)
        assert response['caseId'] == 66
