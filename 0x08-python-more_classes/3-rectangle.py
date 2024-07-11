#!/usr/bin/python3

"""Define a class  Rectangle."""


class Rectangle:
    """ represent rectangle"""

     def __init__(self, width = 0, height = 0):
         """ instansition"""
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """return width"""
        return f"self.__width"
    @width.setter
    def width(self, value):
        """ set width"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
             raise ValueError("width must be >= 0")
    @property
    def height(self):
        """return height"""
        return f"{self.__height}"
    @height.setter
    def height(self, value):
        """ set height"""
        #self.__height = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
             raise ValueError("width must be >= 0")
        self.__height = value
    def area(self):
        """return rectangle area"""
        return f"{self.__width*self.__height}"
    def perimeter(self):
        """ return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return f"{(self.__width*2) + (self.__height*2)}"
    def __str__(self):
        """ return readable output"""
        rectangle = ""
        for i in range(0, self.__height):
            rectangle += ("#" * self.__width) + "\n"
        #return rectangle[:-1]
        if self.__width == 0 or self.__height == 0:
            return(rectangle)
