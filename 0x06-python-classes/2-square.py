#!/usr/bin/python3

"""Define a class Square."""


class square:
    """ Represent Square """
    def __init__(self, size = 0):
        """ initialize a new  Square
            args:
                size(int): the size of new Square
        """
        if size in int.__class__:
            pass
        else:
            raise TypeErro("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
