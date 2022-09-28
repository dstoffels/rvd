from robot import Robot
from dinosaur import Dinosaur
import random


class Battlefield:
    def __init__(self):
        self.robot = Robot('Data')
        self.dino = Dinosaur('Littlefoot', 25)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print()
        print(f'####################################')
        print(f'######### Robot v Dinosaur #########')
        print(f'####################################')
        print()

    def battle_phase(self):
        while self.dino.is_alive() and self.robot.is_alive():
            dino_attacks_first = random.choice([True, False])

            if dino_attacks_first:
                self.dino.attack(self.robot)
                self.robot.attack(self.dino)
            else:
                self.robot.attack(self.dino)
                self.dino.attack(self.robot)

    def display_winner(self):
        winner = ''
        if self.dino.is_alive():
            winner = self.dino.name
        else:
            winner = self.robot.name
        print()
        print(f'{winner} is victorious!')
        print()
