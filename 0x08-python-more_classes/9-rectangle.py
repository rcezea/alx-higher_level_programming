#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle
by: (based on 1-rectangle.py)"""


class Rectangle:
    """Rectangle class succesfully created"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializes the private attributes"""
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        rec = []
        for i in range(self.__height):
            row = ''
            for i in range(self.__width):
                row += "#"
            rec.append(row)
        return "\n".join(rec)

    def __repr__(self):
        return str("Rectangle ("+str(self.__width)+", "+str(self.__height)+")")

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """returns the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        area = self.__width*self.__height
        return area

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            perimeterValue = 0
        else:
            perimeterValue = (self.__width+self.__height)*2
        return perimeterValue

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        a = rect_1.area()
        b = rect_2.area()

        if a >= b:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        cls.__width = size
        cls.__height = size
        return Rectangle(cls.__width, cls.__width)
