#!/usr/bin/python3
"""
function to write in file
"""

import json


def from_json_string(my_str):
    """ function that convert from json to string """
    data = json.loads(my_str)
    return(data)
