#!/usr/bin/python3
""" class mylist """


class MyList(list):
    """ mylist"""

    def __init__(self):
        """ initialization"""
        list.__init__(self)
    def print_sorted(self):
        """ print list in ascending order """
        print(sorted([int(x) for x in list]))
