from kingdom import *


class Primate(Animal):
    def __init__(self, motability, heterotrophy, nervous_system, tissue, alive, limbs, fur, warm_blooded):
        super().__init__(motability, heterotrophy, nervous_system, tissue, alive):
        self.limbs = limbs
        self.fur = fur
        self.warm_blooded = warm_blooded
