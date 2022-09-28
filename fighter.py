import random


class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, target):
        if self.is_alive():
            damage = self.get_damage()
            target.health -= damage
            print()
            print(
                f'{self.name} attacks {target.name} for {damage} damage!')
            print(f'{target.name} has {target.health} health remaining!')
            print()

    def is_alive(self):
        return self.health > 0

    def get_damage(self):
        return random.randint(-10, 10)
