#!/usr/bin/python3
"""
function to write in file
""" 

import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as file:
        data = json.dump(my_obj, file)
        print(data)
