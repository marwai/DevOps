from animal import Animals

class Panda(Animals):
    def __init__(self, name, mood, size, appetite, alive, speed, awake, fat, bamboo):
        super().__init__(name, mood, size, appetite, alive, speed, awake)
        self.fat = fat
        self.bamboo = bamboo

    def bamboo_sticks(self):
        self.bamboo = "low reserves"
        self.speed = "fast"
        self.appetite = "full"
        self.fat = "FAT"
        print(f"{self.name} is now fat but is {self.speed}")

    def time(self):
        self.size = "small"
        print(f"A year has passed {self.name} has gotten bigger!\n")





chewy = Panda(name = "chewy", mood = "content",size = "small", appetite = "low",
              speed = "slow", awake = "tired", fat = "low fat", bamboo = "high reserves", alive = "alive")
chewy.bamboo_sticks()
# chewy.check_status()
# chewy.eat()
# chewy.check_status()
# chewy.time()
# chewy.death()
chewy.check_status()
