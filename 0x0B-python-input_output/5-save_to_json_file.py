#!/usr/bin/python3
"""
function save to json file
""" 

import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file, using a JSON representation """
    with open(filename, "w", encoding="utf-8") as file:
        data = json.dump(my_obj, file)
