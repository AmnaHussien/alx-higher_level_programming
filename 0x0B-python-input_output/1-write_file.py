#!/usr/bin/python3
"""
function to write in file
"""


def write_file(filename="", text=""):
    """ contains write in file and writern the number of character written """
    with open(filename, "r+", encoding="utf-8") as file:
        data_written = file.write(text)
        print(data_written, end="")
        data = file.read()
    print(data)
