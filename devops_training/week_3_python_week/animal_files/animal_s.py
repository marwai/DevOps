class animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("The animal breathes")

    def eat(self):
        print("The animal eats")

    def procreate(self):
        print("The animal breeds")

    def move(self):
        print("The animal moves")