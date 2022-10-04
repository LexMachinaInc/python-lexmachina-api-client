import pytest
import json

from src.lexmachina.client import LexMachinaClient
from configparser import ConfigParser
class TestGetJudges:
    client = LexMachinaClient("config.ini")
    config = ConfigParser()
    config.read("config.ini")
    INTEGER_FUZZ = json.loads(config.get("CONSTANTS", "INTEGER_FUZZ"))

    @pytest.mark.asyncio
    @pytest.mark.parametrize("federal_judges", INTEGER_FUZZ)
    async def test_get_federal_judges_integer_fuzz(self, federal_judges):
        response = await self.client.get_federal_judges(federal_judges=federal_judges)
        assert response.get("detail") == "No judges matching provided judge IDs were found"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("federal_judges", [INTEGER_FUZZ])
    async def test_get_federal_judges_integer_list_fuzz(self, federal_judges):
        response = await self.client.get_federal_judges(federal_judges=federal_judges)
        assert response.get("detail") == "No judges matching provided judges IDs were found"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("magistrate_judges", INTEGER_FUZZ)
    async def test_get_magistrate_judges_integer_fuzz(self, magistrate_judges):
        response = await self.client.get_magistrate_judges(magistrate_judges=magistrate_judges)
        assert response.get("detail") == "No magistrates matching provided magistrate IDs were found"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("federal_judges", [3349, 2421, 2877])
    async def test_get_federal_judges_positive(self, federal_judges):
        response = await self.client.get_federal_judges(federal_judges=federal_judges)
        assert response['federalJudgeId'] == federal_judges

    @pytest.mark.asyncio
    @pytest.mark.parametrize("magistrate_judges", [1437, 141, 174])
    async def test_get_federal_judges_positive(self, magistrate_judges):
        response = await self.client.get_magistrate_judges(magistrate_judges=magistrate_judges)
        assert response['magistrateJudgeId'] == magistrate_judges

    @pytest.mark.asyncio
    @pytest.mark.parametrize("q", ["Sneed"])
    async def test_search_law_firms(self, q):
        response = await self.client.search_judges(q=q)
        assert any(i['name'] == 'Joseph Tyree Sneed III' for i in response['federalJudges'])
        assert any(i['name'] == 'Julie S Sneed' for i in response['magistrateJudges'])
