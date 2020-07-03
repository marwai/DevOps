from animal import Animals

class Panda(Animals):
    def __init__(self, name, mood, size, appetite, alive, speed, awake, fat, bamboo,activity,lazy = True):
        super().__init__(name, mood, size, appetite, alive, speed, awake,fat)
        self.fat = fat
        self.bamboo = bamboo
        self.activity = activity
        self.lazy = lazy

    # specific to pandas so not in animals class
    def bamboo_sticks(self):
        self.bamboo = "low reserves"
        self.speed = "fast"
        self.appetite = "full"
        self.fat = "FAT"
        self.lazy = "False"
        print(f"{self.name} is now fat but is {self.speed}\n")

    # pandas are nocturnal so will be awake at night
    def night(self):
        self.awake = "awake"



    def climb(self):
        if self.lazy == True:
            self.activity = "on the ground"
        else:
            self.activity = "climbing a tree"

# panda panda's name chewy has been set, with set values)
chewy = Panda(name = "chewy", mood = "content", size = "small", appetite = "low", activity= "sitting around",
              speed = "slow", awake = "tired", fat = "low fat", bamboo = "high reserves", alive = "alive" )

# chewy.time()
# chewy.leaves()
# chewy.fatigue()
# chewy.night()
# chewy.bamboo_sticks()
# chewy.death()
# chewy.check_status()

# Encapsulation
# chewy.__size() = 30
# chewy.set_size(30) # only these variables can be printed and not edited due to __
# print(chewy.set_size(30))
# print(chewy.__size())