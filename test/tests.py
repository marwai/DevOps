# for x in range(6):
#     print(x)

class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class hi(Person):
  pass

x = hi("Mike")
x.printname()
