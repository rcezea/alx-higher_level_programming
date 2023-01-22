#!/usr/bin/python3
""" Write a class Square that defines a square """


class Square:
    """ initalization of the class attributes and methods"""
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if isinstance(position, tuple):
            self.__position = position
        else:
            raise TypeError("""position must be a tuple of 2\
            position integers""")

    """ definition of the public method to return area"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            self.__position = value
        else:
            raise TypeError("""position must be a tuple of 2\
            positive integers""")

    def area(self):
        return self.__size*self.__size

    def my_print(self):
        """Prints a square"""
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" "*self.position[0], end="")
            print('#'*self.size)
