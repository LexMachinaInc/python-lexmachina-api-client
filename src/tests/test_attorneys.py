import pytest

from src.lexmachina.client import LexMachinaClient


class TestGetAttorneys:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    @pytest.mark.parametrize("attorney_id", [0, -2, 999999999])
    async def test_get_attorney_integer_fuzz(self, attorney_id):
        response = await self.client.get_attorneys(attorneys=attorney_id)
        assert response.get("detail") == "No attorney matching provided attorney ID was found"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("attorney_id", [110161257, 43337, 14974596])
    async def test_get_attorney_positive(self, attorney_id):
        response = await self.client.get_attorneys(attorneys=attorney_id)
        assert response['attorneyId'] == attorney_id
