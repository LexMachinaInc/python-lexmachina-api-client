import pytest

from . import INTEGER_FUZZ
from src.lexmachina.client import LexMachinaClient


class TestGetParties:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    @pytest.mark.parametrize("parties", INTEGER_FUZZ)
    async def test_get_parties_integer_fuzz(self, parties):
        response = await self.client.get_parties(parties=parties)
        assert response.get("detail") == "No party matching provided party ID was found"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("parties", [2273, 58589403, 73224])
    async def test_get_parties_positive(self, parties):
        response = await self.client.get_parties(parties=parties)
        assert response['partyId'] == parties

    @pytest.mark.asyncio
    @pytest.mark.parametrize("q", ["Apple"])
    async def test_search_parties(self, q):
        response = await self.client.search_parties(q=q)
        assert any(i['name'] == 'Apple Computer, Inc.' for i in response['parties'])
