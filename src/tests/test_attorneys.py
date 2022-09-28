import pytest

from src.lexmachina.client import LexMachinaClient


class TestGetAttorneys:

    @pytest.mark.parametrize("attorney_id", [0, -2, 999999999])
    async def test_get_attorney_integer_fuzz(self, attorney_id):
        response = await LexMachinaClient.get(f'/attorneys/{attorney_id}')
        print(response)
