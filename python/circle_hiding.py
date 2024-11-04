import math
class circle:
    def __init__(self,radius = 1):
        self.__radius = radius

    def setRadius(self,radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

c = circle()
print(c.getRadius())
c.setRadius(2)
print(c.getRadius())


