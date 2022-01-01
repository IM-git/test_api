import pytest
import requests
from src.enums.global_enums import GlobalErrors
from jsonschema import validate
from src.schemas.post import POST_SCHEMA
from src.baseclasses.response import Response
from src.pydantic_shemas.post import Post
from src.schemas.user import User
from configuration import *


@pytest.mark.production     # pytest -s -v -k production test/something_test.py
def test_url(get_users):
    Response(get_users)


@pytest.mark.production
@pytest.mark.skip("Example of skip a test.")
def test_skip():
    pass


@pytest.mark.development    # pytest -s -v -k development test/something_test.py
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, 2, 1),
    (-1, -2, -3),
    ('a', 2, None),
    ('a', 'b', None)
])
def test_calculate(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result
