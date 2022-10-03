import pytest

from src.lexmachina.client import LexMachinaClient


class TestListCourts:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_courts(self):
        response = await self.client.list_courts()
        assert any(i['type'] == 'FederalDistrict' for i in response)
        assert any(i['name'] == 'U.S. District Court for the District of Oregon' for i in response)
        assert any(i['abbreviation'] == 'ohsd' for i in response)