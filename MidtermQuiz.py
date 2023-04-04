#Made by Sergio, Jasper D.
class DistanceConversion:
    def __init__(self, distance):
        self.__distance = distance

    def inch(self):
        return self.__distance * 39.37      #Converts input to inches

    def cm(self):
        return self.__distance * 100        #Converts input to centimeters

    def km(self):
        return self.__distance/1000         #Converts input to Kilometers

    def display(self):
        print(f"You've input {self.__distance} in Meters, this is converted to")
        print(f"{self.cm()} cm in centimeters.")
        print(f"{self.km()} km in kilometers.")
        print(f"And {self.inch()} inches in inch")

m = float(input("Welcome User! Please input the number of Meters to convert: "))        #Receives input
dist = DistanceConversion(m)
dist.display()