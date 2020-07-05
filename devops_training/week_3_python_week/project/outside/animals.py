class Animals:
    def __init__(self, name, health, strength, intelligence, speed, agility, alive ):
        # Attributes (variables in a class)
        self.name = name
        self.health = health
        self.strength = strength
        self.intelligence = intelligence
        self.speed = speed
        self.agility = agility
        self.alive = alive

    def death(self):
        self.alive =False
        print(f" {self.name}  has passed away!\n")

    def check_status(self):
        if self.alive == True:
            print(f"{self.name}'s HP: ", self.health)
            print(f"{self.name} STR: ", self.strength)
            print(f"{self.name}'s INT: ", self.intelligence)
            print(f"{self.name} SPD: ", self.speed)
            print(f"{self.name}  AGL:", self.agility)

    # characterstics of an Animal

    # methods are defined (functions in a class)
    # f"{}" format variables
    # def time(self):
    #     self.size = "big"
    #     print(f"A year has passed {self.name} has gotten bigger!\n")
    #
    #
    # def get_size(self):
    #     return self.__speed
    # #   set panda size (abstraction)
    #
    # def set_size(self,value):
    #     self.__size = value
    #
    # # eats leaves
    # def leaves(self):
    #     self.appetite = "satisfied"#
    #     self.fat = "moderate"
    #     print(f" {self.name} ate some leaves is feeling {self.appetite}\n")
    #
    # # More fatigued the panda, more tired it is and affects how awake it is
    # def fatigue(self):
    #     self.awake = "tired"
    #     print(f"Go to sleep {self.name} you must be very tired!\n")
    #
    # # if the animal dies, it's alive status will be false
    # def death(self):
    #     self.alive =False
    #     print(f" {self.name}  has passed away!\n")
    #
    # # rather than printing every individual attribute,
    # # check status recalls the name {self.name} in this case is the panda's name and prints messages according to each
    # # attribute
    # def check_status(self):
    #     if self.alive == True:
    #         print(f"{self.name}'s mood:", self.mood)
    #         print(f"{self.name} current size:", self.__size)
    #         print(f"Hunger levels of {self.name}'s:", self.appetite)
    #         print(f"{self.name} speed:", self.speed)
    #         print(f"{self.name} fatigue level:", self.awake)
    #         print(f"{self.name} bamboo levels:", self.bamboo)
    #         print(f"{self.name} fat levels:", self.fat)
    #         print(f"{self.name} is currently:", self.activity)
    #         print(f"{self.name} is lazy:", self.lazy)
    #     return
