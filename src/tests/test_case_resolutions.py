import pytest

from src.lexmachina.client import LexMachinaClient


class TestListCaseResolutions:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_get_case_resolutions(self):
        response = await self.client.list_case_resolutions()
        assert any(i['summary'] == 'Claimant Win' for i in response)
        assert any(i['specific'] == 'Trial' for i in response)
        assert any(i['summary'] == 'Procedural' for i in response)
