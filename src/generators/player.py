from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization
from src.baseclasses.builder import BuilderBaseClass


class Player(BuilderBaseClass):

    def __init__(self):
        super().__init__()
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

