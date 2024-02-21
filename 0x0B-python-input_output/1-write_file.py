#!/usr/bin/python3
"""
function to write in file
"""


def write_file(filename="", text=""):
    """ contains write in file and writern the number of character written """
    with open(filename, "w", encoding="utf=8") as file:
        data = file.write(text)
        return(data)
