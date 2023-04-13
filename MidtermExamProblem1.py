import math
# Code Made by Sergio, Jasper D.
pi = math.pi  # Imports pi from math library


class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def perimeter(self):
        return round(2 * pi * self.__radius, 4)  # Calculates Perimeter and rounds it to four

    def area(self):
        return round(pi * self.__radius ** 2, 4)  # Calculates area and rounds it to four

    def display(self):
        print(f"You've input {self.__radius} as the radius,")
        print(f"The perimeter of the Circle is {self.perimeter()} and its area is {self.area()}")  # displays input and calculation


c = float(input("Please input the radius of the circle: "))
dis = Circle(c)
dis.display()
