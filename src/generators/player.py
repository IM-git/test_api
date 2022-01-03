from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization


class Player:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result["account_status"] = status
        return self

    def set_balance(self, balance=2):
        self.result["balance"] = balance
        return self

    def set_avatar(self, avatar="https://images.app.goo.gl/rQYVyagM9QiS2jMXA"):
        self.result["avatar"] = avatar
        return self

    def reset(self):
        self.set_status()
        self.set_balance()
        self.set_avatar()
        self.result["localize"] = {
            "en": PlayerLocalization('en_US').build(),
            "ru": PlayerLocalization('ru_RU').build()
        }
        return self

    def update_inner_generator(self, key, generator):
        self.result[key] = {"en": generator.build()}
        return self

    def build(self):
        return self.result


c = Player().build()
print(c)
print(Player().set_balance(9999).set_status("DELETED").build())