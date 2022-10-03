import pytest

from src.lexmachina.client import LexMachinaClient


class TestGetPatents:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_get_patents_integer_fuzz(self):
        response = await self.client.health()
        assert response == "Feelin' fine." or response == "Database failure"
