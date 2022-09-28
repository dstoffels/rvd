from fighter import Fighter


class Dinosaur(Fighter):
    def __init__(self, name, attack_power):
        self.attack_power = attack_power
        super().__init__(name)

    def get_damage(self):
        randint = super().get_damage()
        return self.attack_power + randint
