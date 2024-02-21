#!/usr/bin/python3
"""
Contains the clas "Student"
"""


class Student:
    """Representation of astudent"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns adictionary representation of aStudent instance"""
        return self.__dict__
