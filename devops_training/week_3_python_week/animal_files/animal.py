# Parent class
class Animals:
    def __init__(self, name, mood, size, appetite, alive, speed, awake,fat):
        # Attributes (variables in a class)
        self.name = name
        self.mood = mood
        self.size = size
        self.appetite = appetite
        self.alive = True
        self.speed = speed
        self.awake = awake
    # characterstics of an Animal
    # methods are defined (functions in a class)
    # f"{}" format variables
    def time(self):
        self.size = "big"
        print(f"A year has passed {self.name} has gotten bigger!\n")

    # eats leaves
    def leaves(self):
        self.appetite = "satisfied"#
        self.fat = "moderate"
        print(f" {self.name} ate some leaves is feeling {self.appetite}\n")

    def fatigue(self):
        self.awake = "tired"
        print(f"Go to sleep {self.name} you must be very tired!\n")

    def death(self):
        self.alive =False
        print(f" {self.name}  has passed away!\n")

    def check_status(self):
        if self.alive == True:
            print(f"{self.name}'s mood:", self.mood)
            print(f"{self.name} current size:", self.size)
            print(f"Hunger levels of {self.name}'s:", self.appetite)
            print(f"{self.name} speed:", self.speed)
            print(f"{self.name} fatigue level:", self.awake)
            print(f"{self.name} bamboo levels:", self.bamboo)
            print(f"{self.name} fat levels:", self.fat)
            print(f"{self.name} is currently:", self.activity)
            print(f"{self.name} is lazy:", self.lazy)


        return
