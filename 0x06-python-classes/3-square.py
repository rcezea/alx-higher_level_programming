#!/usr/bin/python3
""" Write a class Square that defines a square """


class Square:
    """ initalization of the class attributes and methods"""
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """ definition of the public method to return area"""
    def area(self):
        return self.__size*self.__size
