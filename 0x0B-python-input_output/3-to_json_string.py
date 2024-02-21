#!/usr/bin/python3
import json
"""
function to convert into json
"""


def to_json_string(my_obj):
    """  function that returns the JSON representation of an object """
    data = json.dumps(my_obj)
    return(data)
