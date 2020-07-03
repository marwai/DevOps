from animals import *

class Panda(Animals):
    def __init__(self, name, health, strength, intelligence, speed, agility,alive):
        super().__init__(name, health, strength, intelligence, speed, agility,alive)

    def panda_hp(self):
        self.health = 100

    def panda_str(self):
        self.strength = 90

    def panda_int(self):
        self.intelligence = 50

    def panda_int(self):
        self.speed = 55

    def panda_int(self):
        self.agility = 45

Chewy = Panda()
print(Chewy)