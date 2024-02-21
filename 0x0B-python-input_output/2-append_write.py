#!/usr/bin/python3
"""
function to append in file
"""


def append_write(filename="", text=""):
    """ returns the number of chars appended to "filename" from "text" """
    with open(filename, 'a', encoding='utf=8') as file:
        data = file.write(text)
        return(data)
