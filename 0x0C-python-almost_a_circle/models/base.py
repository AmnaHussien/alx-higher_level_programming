#!/usr/bin/python3
"""
contain classes
"""


class Base:
    __nb_objects = 0

    def __init__(self, _id=None):
        " initialization "
        if id is  None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = _id
