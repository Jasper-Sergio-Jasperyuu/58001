class Person:
  def  __init__(self, name, pre, mid, fin):
    self.__name = name
    self.__pre = pre
    self.__mid = mid
    self.__fin = fin
  def Average(self):
    self.__total =  self.__pre + self.__mid + self.__fin
    return round(self.__total/3, 2)
  def  Grade(self):
    print(f"The Grade of {self.__name} is {self.Average()}")

std1 = Person("Student 1", 97, 98, 99)
std1.Grade()
std2 = Person("Student 2", 95, 89, 98 )
std2.Grade()
std3 = Person("Student 3", 86, 89, 90)
std3.Grade()