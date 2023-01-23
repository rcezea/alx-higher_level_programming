#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle
by: (based on 1-rectangle.py)"""


class Rectangle:
    """Rectangle class succesfully created"""
    def __init__(self, width=0, height=0):
        """initializes the private attributes"""
        self.__width = width
        self.__height = height

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
