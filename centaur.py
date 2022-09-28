from fighter import Fighter
from weapon import Weapon


class Centaur(Fighter):
    def __init__(self, name):
        self.active_weapon = Weapon('Spear', 25)
        super().__init__(name)

    def get_damage(self):
        randint = super().get_damage()
        return self.active_weapon.attack_power + randint
