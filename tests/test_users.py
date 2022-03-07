import pytest
from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statuses
from src.schemas.computer import Computer
from examples import computer


@pytest.mark.parametrize("status", Statuses.list())
def test_something(status, get_player_generator):
    """Generated list with player's values."""
    print(get_player_generator.build())


@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_deleted_all_keys(delete_key, get_player_generator):
    """Deleted all keys in dictionary step by step."""
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


def test_add_new_key_in_dictionary(get_player_generator):
    """Add new key in dictionary and change value in localization."""
    object_to_send = get_player_generator.update_inner_value(
        ['localize', 'en', 'countries'], PlayerLocalization('fr_FR').set_number(15).build()
    ).build()
    print(object_to_send)


@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR")
])
def test_something_with_parametrize(get_player_generator, localizations, loc):
    """Add new key in dictionary and change value in localization."""
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations], PlayerLocalization(loc).set_number(15).build()
    ).build()
    print(object_to_send)


def test_pydantic_object():
    comp = Computer.parse_obj(computer)
    print(comp.detailed_info.physical.color)
