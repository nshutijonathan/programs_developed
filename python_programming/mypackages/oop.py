import math
class Rectangle:
    def __init__(self, color, filled, width, length):
        self.__color = color
        self.__filled = filled
        self.__width = width
        self.__length = length

    def get_color(self):
        return self.__color

    def set_color(self, color):
        return self.color

    def is_filled(self):
        return self.__filled

    def set_filled(self,):
        print("amen")

    def get_area():
        return self.__width * self.__length

class Circle:
    def __int__(self, color, filled, radius):
        self.__color = color
        self.__filled = filled
        self.__radius = radius      

    def get_color(self):
        return self.__color

    def set_color(self, color):
        return self.__color

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        return self.__filled

    def get_area(self):
        return math.pi * self.__radius ** 2
d=Rectangle("kki","jk","ds","ds")
print(d.set_filled())
