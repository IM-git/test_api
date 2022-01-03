import pytest
from src.generators.player_localization import PlayerLocalization


@pytest.mark.parametrize("status", [
    "ACTIVE",
    "BANNED",
    "DELETED",
    "INACTIVE"
])
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
    object_to_send = get_player_generator.update_inner_generator(
        'localize', PlayerLocalization('fr_FR').set_number(15)
    ).build()
    print(object_to_send)
