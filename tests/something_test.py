import pytest
from src.baseclasses.response import Response


@pytest.mark.production     # pytest -s -v -k production test/something_test.py
def test_url(get_users):
    """ Received a response from the website. """
    Response(get_users)


@pytest.mark.production
@pytest.mark.skip("Example of skip a test.")
def test_skip():
    """ Checking how to skip test method. """
    pass


@pytest.mark.production
def test_with_error():
    """ In that test we try to check that first value is equal to second value. """
    assert 12 == 21


@pytest.mark.development    # pytest -s -v -k development test/something_test.py
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, 2, 1),
    (-1, -2, -3),
    ('a', 2, None),
    ('a', 'b', None)
])
def test_calculate(first_value, second_value, result, calculate):
    """ Comparing calculating method with expected calculating value(Valid and invalid). """
    assert calculate(first_value, second_value) == result
