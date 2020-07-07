class Car:
    def __init__(self, speed, color):
        super().__()
        # __speed and __color has been to set to private to prevent accidentally changing the variable
        self.__speed = speed
        self.__color = color

    # set attribute (set attr) has to be called to change the speed
    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed


    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color

ford = Car(200, 'red')
honda = Car(250, 'blue')
audi = Car(300, 'black')

ford.set_speed(300)
# ford.__speed = 400 # uncommenting this will produce an error because speed has been set to a private variable
print(ford.get_speed())
# ford.__color # will also produce an error
print(ford.get_color())