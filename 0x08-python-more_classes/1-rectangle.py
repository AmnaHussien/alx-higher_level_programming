#!/usr/bin/python3

"""Define a class  Rectangle."""


class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return f"self.__width"
    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
             raise ValueError("width must be >= 0")
    @property
    def height(self):
        return f"{self.__height}"
    @height.setter
    def height(self, value):
        #self.__height = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
             raise ValueError("width must be >= 0")
        self.__height = value
