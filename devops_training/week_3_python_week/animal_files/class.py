from animal import Animals


class Primate(Animals):
    def __init__(self, name, motability, heterotrophy,  tissue, alive, limbs, fur, warm_blooded):
        super().__init__(motability, heterotrophy, tissue, alive)
        self.limbs = limbs
        self.fur = fur
        self.warm_blooded = warm_blooded
        self.name = name


    def limbs(self):
        self.limbs = "has four limbs"

    def fur(self):
        self.fur = "has fur"

    def warm_blooded(self):
        self.warm_blooded = "warm blooded"

    def check_status(self):
        print(f"is {self.name} sleepy?", self.motability)
        print(f"is {self.name} sleepy?", self.heterotrophy)
        print(f"How is {self.name}'s hunger levels?", self.tissue)
        print(f"what is {self.name}'s mood?", self.alive)
        print(f"what species is {self.name}?", self.limbs)
        print(f"what species is {self.name}?", self.fur)
        print(f"what species is {self.name}?", self.warm_blooded, "\n")

Marcus = Primate("moving", "eating well", "tissues working", "alive", "has two limbs", "hi" , fur="furry",warm_blooded="hot")
