#!/usr/bin/python3
"""
function to write in file
"""

import json


def load_from_json_file(filename):
    """ a function that creates an Object from a “JSON file” """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        return(data)
