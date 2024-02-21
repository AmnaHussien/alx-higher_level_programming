#!/usr/bin/python3
"""
read file function
"""


def read_file(filename=""):
    """ function that read utf-8 and print it to stdout """
    with open(filename, "r", encoding = "utf-8") as file:
        data = file.read()
        print(data, end = "")
