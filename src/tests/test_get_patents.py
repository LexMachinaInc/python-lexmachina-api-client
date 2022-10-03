import pytest

from src.lexmachina.client import LexMachinaClient


class TestGetPatents:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    @pytest.mark.parametrize("patents", [0, -2, 999999999])
    async def test_get_patents_integer_fuzz(self, patents):
        response = await self.client.get_patents(patents=patents)
        assert response.get("detail") == "No patent matching provided patent number was found"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("patents", [6904359, 6714859, 5668543])
    async def test_get_patents_positive(self, patents):
        response = await self.client.get_patents(patents=patents)
        assert response['number'] == str(patents)
