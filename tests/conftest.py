import pytest
import requests
from configuration import SERVICE_URL
from src.generators.player import Player


@pytest.fixture
def get_player_generator():
    return Player()


@pytest.fixture
def get_users():
    return requests.get(SERVICE_URL)


def _calculate(first_value, second_value):
    if isinstance(first_value, int) and isinstance(second_value, int):
        return first_value + second_value
    else:
        return None


@pytest.fixture
def calculate():
    return _calculate
